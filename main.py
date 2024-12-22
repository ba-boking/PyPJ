from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import csv

app = FastAPI()

sol = {
    "low": "기본적인 건강 관리 및 생활 지원.",
    "medium": "노인 돌봄 서비스 강화 및 교통 인프라 개선.",
    "high": "고령자 전용 주택 개발, 의료 시스템 강화 및 사회적 지원 확대."
}

@app.get("/")
def root():
    return {"message": "Busan 고령화 서비스"}

@app.get("/age/{gu}", response_class=HTMLResponse)
def age(gu: str):
    data = {}
    with open('age.csv', 'r', encoding='utf-8') as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            data[row[0]] = float(row[3])
    
    if gu in data:
        a = data[gu]
        if a < 15:
            soln = sol["low"]
        elif a < 30:
            soln = sol["medium"]
        else:
            soln = sol["high"]
        
        return f"""
        <html>
            <head><title>{gu} 고령화 대응</title></head>
            <body>
                <h1>{gu} 고령화 해결책</h1>
                <p>고령화 수준: {a}세</p>
                <p>해결책: {soln}</p>
            </body>
        </html>
        """
    return f"<html><body><h1>{gu} 데이터 없음</h1></body></html>"
