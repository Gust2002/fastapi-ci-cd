from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/hello")
def Hello_world():
    return {"Message" "Hello guys"}


my_library = {}

@app.get("/requesting")
def get_book(id_book: int, book_name: str, author_name: str, book_year: int):
 if not my_library:
    return {"Message": "This book does not exist"}
 else:
     return {"get_book": my_library}
 
@app.post("/creating")
def post_book(id_book: int, book_name: str, author_name: str, book_year):
    if id_book in my_library:
        raise HTTPException(status_code=400,detail="This book is created already")
    else:
        my_library[id_book] = {"book_name": book_name, "author_name": author_name, "book_year": book_year}
        
        return {"Message": "Your book has been created with suceafully!!"}
    
@app_put("/update/{id_book}")
def put_book(id_book: int, book_name: str, author_name: str, book_year: int):
    book = my_library.get[id_book]
    if not book:
        raise HTTPException(status_code=404,detail="This book was not found on the system")
    else:
        if book_name:
         book_name["book_name"] = book_name
        if author_name:
         author_name["author_name"] = author_name
        if book_year:
         book_year["book_year"] = book_year
    
    return {"Message": "Your book has been update with sucesfully"} 

@app.delete("/delete/{id_book}")
def delete_book(id_book: int, book_name: str, author_book: str, year_book: int):
    if id_book not in my_library:
        raise HTTPException(status_code=500,detail="This book was not found on the system")
    else:
        del my_library[id_book]