from fastapi import FastAPI, Form, Request
from transformers import pipeline
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

templates = Jinja2Templates(directory='htmldirectory')

app = FastAPI()
translator = pipeline("translation_ru_to_en", model=model, tokenizer=tokenizer)


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse('home.html',{'request': request})


def predict(df: str):
    return translator(df)[0]


@app.post("/",response_class=HTMLResponse)
async def handle_form(request: Request, assignment: str = Form(...)):
    return templates.TemplateResponse('home.html',{'request': request, 'result': predict(assignment)})
