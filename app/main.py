from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/organizations/")
def get_organizations(db: Session = Depends(get_db)):
    return crud.get_organizations(db)

@app.get("/organizations/{organization_id}")
def get_organization(organization_id: int, db: Session = Depends(get_db)):
    return crud.get_organization(organization_id, db)

@app.get("/organizations/by-building/{building_id}")
def get_organizations_by_building(building_id: int, db: Session = Depends(get_db)):
    return crud.get_organizations_by_building(building_id, db)

@app.get("/organizations/by-activity/{activity_id}")
def get_organizations_by_activity(activity_id: int, db: Session = Depends(get_db)):
    return crud.get_organizations_by_activity(activity_id, db)

@app.get("/organizations/search/")
def search_organization_by_name(name: str, db: Session = Depends(get_db)):
    return crud.search_organization_by_name(name, db)

@app.get("/organizations/by-activity-tree/{activity_id}")
def get_organizations_by_activity_tree(activity_id: int, db: Session = Depends(get_db)):
    return crud.get_organizations_by_activity_tree(activity_id, db)