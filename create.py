from application import db
from application.models import Collections, Drmartens, Itemslist, Users

db.drop_all()
db.create_all()

ShoeData1 = Drmartens(name="1460 SMOOTH LEATHER ANKLE BOOTS", style_code="25714659", itemslist_id="1")
ShoeData2 = Drmartens(name="JADON MAX PLATFORM BOOTS", style_code="25566001", itemslist_id="2")
ShoeData3 = Drmartens(name="1B60 XL LEATHER PLATFORM BOOTS", style_code="25753001", itemslist_id="3")
ShoeData4 = Drmartens(name="COMBS TECH UTILITY BOOTS", style_code="25216355", itemslist_id="4")
ShoeData5 = Drmartens(name="SHRIVER HI LEATHER LACE UP BOOTS", style_code="24490606", itemslist_id="5")
ShoeData6 = Drmartens(name="HOLLY IRIDESCENT LEATHER PLATFORM SHOES", style_code="25236650", itemslist_id="6")
ShoeData7 = Drmartens(name="ZUMA II LEATHER BOOTS", style_code="25713001", itemslist_id="7")
ShoeData8 = Drmartens(name="1460 SPARKLE BOOTS", style_code="25562308", itemslist_id="8")
ShoeData9 = Drmartens(name="2976 SMOOTH LEATHER CHELSEA BOOTS", style_code="22227001", itemslist_id="9")
ShoeData10 = Drmartens(name="1460 HARNESS LEATHER ANKLE BOOTS", style_code="25163001", itemslist_id="10")
db.session.add(ShoeData1)
db.session.add(ShoeData2)
db.session.add(ShoeData3)
db.session.add(ShoeData4)
db.session.add(ShoeData5)
db.session.add(ShoeData6)
db.session.add(ShoeData7)
db.session.add(ShoeData8)
db.session.add(ShoeData9)
db.session.add(ShoeData10)
db.session.commit()