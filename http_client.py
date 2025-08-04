from aiohttp import ClientSession

from database import get_likes_by_genre

class HTTPClient:
    def __init__(self, base_url: str):
        self._session = ClientSession(
            base_url=base_url,
        )


class OPLHTTPClient(HTTPClient):
    async def get_books_by_genre(self, genre: str, username: str):
        async with self._session.get(
            f'/subjects/{genre}.json?limit=100',
        ) as resp:
            data = await resp.json()
            result = []
            liked_books = get_likes_by_genre(genre, username)
            for el in data["works"]:
                book_info = {}
                book_info["title"] = el["title"]

                if el["title"] in liked_books:
                    book_info["liked"] = True
                else:
                    book_info["liked"] = False
                if el["authors"]:
                    book_info["authors"] = el["authors"][0]["name"]
                    for i in range(1, len(el["authors"])):
                        if el["authors"][i]["name"] not in book_info:
                            book_info["authors"] += ', ' + el["authors"][i]["name"]
                else:
                    book_info["authors"] = "Unknown"

                if book_info not in result:
                        result.append(book_info)

            return result