from sqlalchemy.orm import Session

from db.models.stats import Stats
from schemas.stats import StatsCreate

from datetime import datetime


def create_stats(stats: StatsCreate, db: Session):
    category = Stats(
        date=stats.date,
        views=stats.views,
        clicks=stats.clicks,
        cost=stats.cost
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update_stats(id: int, stats: StatsCreate, db: Session):
    existing_stats = db.query(Stats).filter(Stats.id == id)
    if not existing_stats.first():
        return 0
    stats.__dict__.update()
    existing_stats.update(stats.__dict__)
    db.commit()
    return 1


def get_stats(id: str, db: Session):
    stats = db.query(Stats).filter(Stats.id == id).first()
    return stats


def list_stats(from_date: datetime.date, to_date: datetime.date, db: Session):
    return db.query(Stats).filter(Stats.date >= from_date, Stats.date <= to_date).order_by(Stats.date).all()


def delete_all_stats(db: Session):
    db.query(Stats).delete()
    db.commit()
    return 1
