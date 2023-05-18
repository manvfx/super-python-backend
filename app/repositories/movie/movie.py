import typing
import motor

from app.models.movie import Movie
from app.repositories.movie.abstractions import MovieRepository, RepositoryException


class MemoryMovieRepository(MovieRepository):
    async def __init__(self):
        self._storage = {}

    async def create(self, movie: Movie):
        self._storage[movie.id] = movie

    async def get_by_id(self, movie_id: str) -> typing.Optional[Movie]:
        return self._storage.get(movie_id)

    async def get_by_title(self, title: str) -> typing.List[Movie]:
        return_value = []
        for _, value in self._storage.items():
            if title == value.title:
                return_value.append(value)
        return return_value

    async def delete(self, movie_id: str):
        self._storage.pop(movie_id, None)
        if movie is None:
            raise RepositoryException(f"Movie: {movie_id} not found")
        for key, value in update_parameters.items():
            if key == "id":
                raise RepositoryException(f"can't update movie id")
            if hasattr(movie, key):
                setattr(movie, key, value)

    async def update(self, movie_id: str, update_parameters: dict):
        movie = self._storage


class MovieMongoRepository(MovieRepository):
    def __init__(self, connection_string: str = 'mongodb://localhost:27017'):
        self._clinet = motor.motor_asyncio.AsyncIOMotorClient(
            connection_string)
        self._database = self._clinet["movie_track_db"]
        self._movies = self._database["movies"]

    async def create(self, movie: Movie):
        await self._movies.insert_one(movie)

    async def get_by_id(self, movie_id: str) -> typing.Optional[Movie]:
        await self._movies.find_one({"id": movie_id})

    async def get_by_title(self, title: str) -> typing.List[Movie]:
        pass

    async def delete(self, movie_id: str):
        pass

    async def update(self, movie_id: str, update_parameters: dict):
        pass
