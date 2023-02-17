from fastapi import APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from fastapi.responses import JSONResponse, Response
from fastapi import status
from fastapi import HTTPException

from sqlalchemy.orm import Session

from db.session import get_db
from schemas.stats import StatsCreate, StatsShow
from db.repository.stats import create_stats, update_stats, get_stats, list_stats, delete_all_stats


router = APIRouter()


@router.post("/", summary="Сохранение статистики")
async def save_stats(stats: StatsCreate, db: Session = Depends(get_db)):
    """
    Метод сохранения статистики
    :param stats: Данные по статистике.
    :param db: База данных (берется из зависимости)
    :return: Респонс.
    """
    try:
        create_stats(stats=stats, db=db)
        return Response(status_code=201)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ошибка сохранения статистики"
        )


@router.post("/show_stats", summary="Показ статистики")
async def show_stats(date_stats: StatsShow, db: Session = Depends(get_db)):
    """
    Метод показа статистики
    :param date_stats: Данные по временному промежутку
    :param db: База данных (берется из зависимости)
    :return: Список статситик по возрастанию Даты.
    """
    try:
        all_stats = list_stats(from_date=date_stats.from_date, to_date=date_stats.to_date, db=db)
        result = list()
        for current_stats in all_stats:
            result.append({
                "date": str(current_stats.date),
                "views": current_stats.views,
                "clicks": current_stats.clicks,
                "cost": current_stats.cost,
                "cpc": current_stats.cost / current_stats.clicks if current_stats.clicks else 0,
                "cpm": (current_stats.cost / current_stats.views) * 1000 if current_stats.views else 0
            })
        resp = {
            "result": result
        }
        return JSONResponse(content=resp, status_code=200)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ошибка показа статистики"
        )


@router.get("/delete_stats", summary="Удаление всей статистики")
async def delete_stats(db: Session = Depends(get_db)):
    """
    Метод удаления всех статистик.
    :param db: База данных (берется из зависимости)
    :return: статус код 200.
    """
    try:
        delete_all_stats(db=db)
        return Response(status_code=200)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ошибка удаления статистики"
        )
