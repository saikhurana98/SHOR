DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS product;

CREATE TABLE user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  name TEXT,
  address TEXT,
  contact TEXT,
  email TEXT,
  wishlist TEXT,
  myorders TEXT
);


CREATE TABLE post(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
);

CREATE TABLE product(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  category INTEGER NOT NULL,
  code TEXT NOT NULL,
  name TEXT NOT NULL,
  image TEXT NOT NULL,
  describe TEXT NOT NULL,
  price INTEGER
);


INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (1, 'Berehem Duniya T Shirt', 0,'Men_prod1', '/static/img/actual/Screen_Shot_2019-09-17_at_6.18.38_PM.png', 'Front: "Berehem duniya" (unforgiving world in Hindi), Back: graphic picture of a rickshaw puller. Material: 100% cotton, custom-printed', 599);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (2,  'NEW DELHI Hoodie' , 0,  'Men_prod2' ,  '/static/img/actual/new delhi hoodie site1.jpg',  '"NEW DELHI" written on front with नई दिल्ली written on the sides and a Delhi metro graphic on the back. Material: 100% cotton, custom-printed' , 999);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (3,  'Raat aur din T shirt' , 0,  'Men_prod3' , '/static/img/actual/raat aur din2.jpg',  'T shirt with "Raat aur din" written on front with graphic of a market in Delhi. Material: 100% cotton, custom printed.' , 599);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (4,  'Send cuddles T shirt' , 1,  'Women_prod1' , '/static/img/actual/send cuddles mockup.jpg',  'Feel extra comfy in this T shirt which says "Send cuddles" in Hindi! Custom-printed, 100% cotton.' , 599);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (5,  'Seedhe maut T Shirt' , 1,  'Women_prod2' , '/static/img/actual/Screen Shot 2019-10-07 at 3.11.39 AM.png',  'Show your support for the Indian rap duo Seedhe Maut with this custom-made T shirt! 100% cotton, custom-printed.' , 599);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (6,  'Berehem Duniya Sweatshirt' , 1,  'Women_prod3' , '/static/img/actual/berehem sweatshirt.jpg',  'Front: "Berehem duniya" (unforgiving world in Hindi), Sides: Hindi text of berehem duniya, Back: graphic picture of a rickshaw puller. Material: 100% cotton, custom-printed' , 799);

INSERT INTO product (id, name, category, code, image, describe, price)
VALUES (7,  'New Delhi White Tee' , 2,  'Acc_prod1' , '/static/img/actual/Screen Shot 2019-10-02 at 12.42.56 AM.png',  'This T shirt has "NEW DELHI" written on the front along with a metro graphic printed on the back. 100% cotton, custom-printed.' , 599);
