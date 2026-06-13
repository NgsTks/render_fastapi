from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        ("大吉","大吉！素晴らしい幸運が舞い込むでしょう。"),
        ("中吉", "中吉！努力が実を結び、良い結果が待っています。"),
        ("小吉","小吉！ちょっとした幸運があなたの元にやってきます。"),
        ("吉","吉！安定した幸せな日々が続くでしょう。"),
        ("末吉","末吉！努力が実り始め、良い方向に進む時期です。"),
        ("凶","凶。悪いことが起こるかもしれませんが、気を引き締めてください。"),
        ("小凶","小凶。注意が必要な日です。慎重に行動しましょう。"),
        ("大凶","大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。")
    ]
    rand = random.randrange(8)
    return {"result" : omikuji_list[rand][0], "description" : omikuji_list[rand][1]}

from fastapi.responses import HTMLResponse

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fast-API Sample Page</title>
        <style>
            /* デュオトーンのカラーアニメーション設定 */
            @keyframes duotone-animation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            body, html {
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #2c3e50, #e74c3c);
                background-size: 200% 200%;
                animation: duotone-animation 10s ease infinite;
                font-family: 'Arial', sans-serif;
                color: white;
            }

            h1 {
                font-size: 5rem;
                text-transform: uppercase;
                letter-spacing: 0.1rem;
                text-shadow: 2px 4px 10px rgba(0,0,0,0.3);
                text-align: center;
                margin: 0;
                padding: 20px;
            }

            @media (max-width: 768px) {
                h1 { font-size: 3rem; }
            }
        </style>
    </head>
    <body>

        <h1>Fast-API Sample Page</h1>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)