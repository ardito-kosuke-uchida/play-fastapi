from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.models import Post, PostIn
from app.repositories import PostRepository
from app import dependencies


router = APIRouter(prefix="/posts", tags=["posts"])


@router.post(
    "",
    response_model=Post,
    dependencies=[Depends(dependencies.basicauth)],
)

def create(
        post: PostIn,
        repository=Depends(PostRepository),
        account=Depends(dependencies.currentuser),
):
    return repository.create(post, account)


@router.get(
    "/{post_id}",
    response_model=Post,
)
def get(post_id: int, repository=Depends(PostRepository)):
    if (post := repository.get(post_id)) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        return post


@router.get(
    "",
    response_model=List[Post],
)
def list_post(
        page_params=Depends(dependencies.pagination_params),
        repository=Depends(PostRepository),
):
    return repository.list_item(**page_params)
