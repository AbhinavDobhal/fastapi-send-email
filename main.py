import uvicorn
from fastapi import FastAPI, BackgroundTasks
from send_email import send_email_background, send_email_async

app = FastAPI(title='How to Send Email')


@app.get('/')
def index():
    return 'Hello World'


@app.get('/send-email/asynchronous')
async def send_email_asynchronous():
    await send_email_async('Hello World asynchronous', 'abhinav.dobhal@gmail.com', {
        'title': 'Hello World asynchronous',
        'name': 'abhinav Dobhal'
    })
    return 'Success'


@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks, 'Hello World backgroundtasks', 'abhinav.dobhal@gmail.com', {
        'title': 'Hello World ddd',
        'name': 'abhinav Dobhal'
    })
    return 'Success'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
