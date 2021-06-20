from fastapi import APIRouter, Depends, status, HTTPException
from app.models import AccountIn, Account, AccountPatch
from app.repositories import AccountRepository
from app import dependencies


router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post(
    "",
    summary="アカウント作成",
    description="アカウント作成",
    response_model=Account,
)
def create(account_in: AccountIn, repository=Depends(AccountRepository)):
    """ hogehoge """
    return repository.create(account_in)


@router.get(
    "/{account_id}",
    response_model=Account,
    dependencies=[Depends(dependencies.basicauth)],
)
def get(account_id: int, account=Depends(dependencies.currentuser)):
    if account.id != account_id:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        return account


@router.patch(
    "/{account_id}",
    dependencies=[Depends(dependencies.basicauth)],
)
def patch(
    account_id: int,
    account_patch: AccountPatch,
    repository=Depends(AccountRepository),
    account=Depends(dependencies.currentuser),
):
    if account.id != account_id:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return repository.patch(account, account_patch)
