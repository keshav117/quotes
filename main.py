from fastapi import FastAPI, HTTPException
from models import init_db, get_random_quote, search_quotes_by_author

app = FastAPI()

# Initialize the database
init_db()

@app.get("/quote")
async def quote_of_the_day():
    quote = get_random_quote()
    if quote:
        return {"author": quote[0], "quote": quote[1]}
    raise HTTPException(status_code=404, detail="No quotes found")

@app.get("/search")
async def search_quotes(author: str):
    quotes = search_quotes_by_author(author)
    if quotes:
        return [{"author": q[0], "quote": q[1]} for q in quotes]
    raise HTTPException(status_code=404, detail="No quotes found for the author")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
