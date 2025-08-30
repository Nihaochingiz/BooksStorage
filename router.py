from fastapi import APIRouter
from typing import List
from repository import BookRepository
from schemas import BookAdd, BookResponse, BookId

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post("", response_model=BookId)
async def add_book(book: BookAdd) -> BookId:
    new_book_id = await BookRepository.add_book(book)
    return BookId(id=new_book_id)

@router.get("", response_model=List[BookResponse])
async def get_books() -> List[BookResponse]:
    tasks = await BookRepository.get_books()
    return tasks