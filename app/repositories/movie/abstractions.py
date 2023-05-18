import abc
import typing
from app.models.movie import Movie


class RepositoryException(Exception):
    pass


class MovieRepository(abc.ABC):
    def create(self, movie: Movie):
        """
        Creates a movie and returns true on success
        """
        raise NotImplementedError

    def get_by_id(self, movie_id: str) -> typing.Optional[Movie]:
        """
        retrieves a movie by it's Id and if the movie is not found it will return none
        """
        raise NotImplementedError

    def get_by_title(self, title: str) -> typing.List[Movie]:
        """
        returns a list of movies which share the some title
        """
        raise NotImplementedError

    def delete(self, movie_id: str):
        """
        Deletes a movie by it's id
        """
        raise NotImplementedError

    def update(self, movie_id: str, update_parameters: dict):
        """
        Update a movie by it's id
        """
        raise NotImplementedError
