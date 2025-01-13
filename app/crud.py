from sqlalchemy.orm import Session
from . import models
from .models import Organization, Activity

# Получить все организации
def get_organizations(db: Session):
    return db.query(models.Organization).all()

# Получить организацию по ID
def get_organization(organization_id: int, db: Session):
    return db.query(models.Organization).filter(models.Organization.id == organization_id).first()

# список всех организаций находящихся в конкретном здании
def get_organizations_by_building(building_id: int, db: Session):
    return db.query(Organization).filter(Organization.building_id == building_id).all()

# список всех организаций, которые относятся к указанному виду деятельности
def get_organizations_by_activity(activity_id: int, db: Session):
    return db.query(Organization).filter(Organization.activity_id == activity_id).all()

# поиск организации по названию
def search_organization_by_name(name: str, db: Session):
    return db.query(Organization).filter(Organization.name.ilike(f"%{name}%")).all()

# искать организации по виду деятельности. Например, поиск по виду деятельности «Еда», 
# которая находится на первом уровне дерева, и чтобы нашлись все организации, которые относятся к видам деятельности, 
# лежащим внутри. Т.е. в результатах поиска должны отобразиться организации с видом деятельности Еда, Мясная продукция, Молочная продукция.
def get_organizations_by_activity_tree(activity_id: int, db: Session):
    def get_child_activities(activity_id, db):
        children = db.query(Activity).filter(Activity.parent_id == activity_id).all()
        child_ids = [activity.id for activity in children]
        for child in children:
            child_ids.extend(get_child_activities(child.id, db))
        return child_ids

    activity_ids = [activity_id] + get_child_activities(activity_id, db)
    return db.query(Organization).filter(Organization.activity_id.in_(activity_ids)).all()