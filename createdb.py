from Management import db, create_app
from Management import db
from Management.models import Type,States
app=create_app()
ctx=app.app_context()
ctx.push()
db.create_all()
eventCategory = ['Genre - Rock','Genre - Pop','Genre - Electronic','Genre - Dance','Genre - Country','Community','Comedy']

for i in (eventCategory):
    new_data = Type(type = i)
    db.session.add(new_data)

eventState = ['Upcoming', 'Selling Out', 'Sold Out']
 
for i in (eventState):
    new_data_states = States(states = i)
    db.session.add(new_data_states)

db.session.commit()
quit()