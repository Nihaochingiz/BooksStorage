from sqlalchemy import select
from database import BookOrm, new_session
from schemas import BookAdd, BookResponse

class BookRepository:
    @classmethod
    async def add_book(cls, book: BookAdd) -> int:
        async with new_session() as session:
            data = book.model_dump()
            new_book = BookOrm(**data)
            session.add(new_book)
            await session.flush()
            await session.commit()
            return new_book.id

    @classmethod
    async def get_books(cls) -> list[BookResponse]:
        async with new_session() as session:
            query = select(BookOrm)
            result = await session.execute(query)
            book_models = result.scalars().all()
            return [BookResponse.model_validate(book_model) for book_model in book_models]