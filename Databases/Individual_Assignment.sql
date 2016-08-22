CREATE TABLE PHARMACY(
DRUG VARCHAR2 (40),
NON_DRUG VARCHAR2(40),
STOCK_CODE NUMBER (15),
DESCRIPTION VARCHAR2 (100),
PACK_SIZE NUMBER (2),
BRAND_NAME VARCHAR2 (30),
COST_PRICE NUMBER(3),
RETAIL_PRICE NUMBER (3),
DRUG_TYPE VARCHAR2 (15)
);

CREATE TABLE DRUG_TYPE_INFO(
NAME_CUSTOMER VARCHAR2(30),
DOSAGE NUMBER(2),
PRESCRIPTION_ONLY CHAR (1),
DISPENCE_INFO VARCHAR2 (100),
USER_INFO VARCHAR2 (100)
);

CREATE TABLE BRAND_INFO (
STOCK_CODE NUMBER (15),
COST_PRICE NUMBER (3),
RETAIL_PRICE NUMBER (3)
);

CREATE TABLE PRESCRIPTION_INFO (
NAME_CUSTOMER VARCHAR2 (30),
ADDRESS VARCHAR2 (30),
DOC_NAME VARCHAR2 (30),
DOC_ADDRESS VARCHAR2 (30),
DRUG_TYPE VARCHAR2 (20),
DRUG_DOSAGE VARCHAR2 (20),
DAYS_TO_BE_TAKEN NUMBER (3),
MEDICAL_CARD_NUMBER NUMBER (8),
UNIQUE_PRECRIPTION_NUMBER NUMBER (10)
);

CREATE TABLE CARD_INFO (
NAME_CUSTOMER VARCHAR2 (30),
ADDRESS VARCHAR2 (30),
MEDICAL_CARD_NUMBER NUMBER (8)
);

CREATE TABLE DRUG_BOOK (
NAME_CUSTOMER VARCHAR2 (30),
DRUG_DESCRIPTION VARCHAR2 (100),
DRUG_DOSAGE VARCHAR2 (20)
);

CREATE TABLE SALES_BOOK (
PRESCRIPTION_NUMBER NUMBER (10),
STOCK_CODE NUMBER (15),
QUANTITY NUMBER (4),
COST_A NUMBER (3),
MEDICAL_CARD_NUMBER NUMBER (8)
);

CREATE TABLE NON_DRUG_SALES (
DATE_SOLD DATE,
TIME_SOLD NUMBER (4),
STOCK_CODE NUMBER (15),
QUANTITY NUMBER (4),
COST_B NUMBER (3)
);

INSERT INTO PHARMACY(brand_name, cost_price, description, drug, drug_type, non_drug, pack_size, retail_price, stock_code)
VALUES('PARACETEMOL',2,'FOR HEADACHES','PARACETOMOL','PAIN KILLER','0',12,12,123125);

INSERT INTO PHARMACY(brand_name, cost_price, description, drug, drug_type, non_drug, pack_size, retail_price, stock_code)
VALUES('STREPSILES',1,'FOR SOAR THROATS','PARACETOMOL','PAIN KILLER','0',12,5,123127);

INSERT INTO PHARMACY(brand_name, cost_price, description, drug, drug_type, non_drug, pack_size, retail_price, stock_code)
VALUES('THE PILL',20,'CONTACEPTIVE','CONTRACEPTIVE','CONTRACEPTIVE','0',12,30,123576);




INSERT INTO drug_type_info(name_customer, dispence_info, dosage, prescription_only, user_info)
VALUES('JOE','TWICE DAILY','1','Y','TAKE 1 TABLET TWICE DAILY');

INSERT INTO drug_type_info(name_customer, dispence_info, dosage, prescription_only, user_info)
VALUES('NIAMH','ONCE AFTER MEAL','1','Y','TAKE 1 TABLET AFTER A LARGE MEAL');

INSERT INTO drug_type_info(name_customer, dispence_info, dosage, prescription_only, user_info)
VALUES('JORDAN','ONCE EVERY SECOND DAY','1','N','TAKE 1 TABLET EVERY 48 HOURS');





INSERT INTO brand_info(stock_code, cost_price, retail_price)
VALUES('123125',2,12);

INSERT INTO brand_info(stock_code, cost_price, retail_price)
VALUES('123127',1,5);

INSERT INTO brand_info(stock_code, cost_price, retail_price)
VALUES('123576',12,20);





INSERT INTO prescription_info(name_customer,address,days_to_be_taken,doc_address,doc_name,drug_dosage,drug_type,medical_card_number,unique_precription_number)
VALUES('JOE','20 DAILY DRIVE',365,'20 SWEETMOUNT DRIVE','CIARÁN','TWICE DAILY','PAIN KILLER',1345678,678);

INSERT INTO prescription_info(name_customer,address,days_to_be_taken,doc_address,doc_name,drug_dosage,drug_type,medical_card_number,unique_precription_number)
VALUES('NIAMH','20 SYCAMOUR ROAD',120,'20 SWEETMOUNT DRIVE','CIARÁN','ONCE A DAY','PAIN KILLER',134589,679);

INSERT INTO prescription_info(name_customer,address,days_to_be_taken,doc_address,doc_name,drug_dosage,drug_type,medical_card_number,unique_precription_number)
VALUES('JORDAN','28 FITZROY AVE',120,'20 SWEETMOUNT DRIVE','CIARÁN','EVERY SECOND DAY','CONTRACEPTIVE',134592,680);




INSERT INTO card_info(name_customer, address, medical_card_number)
VALUES('JOE','20 DAILY DRIVE',1345678);

INSERT INTO card_info(name_customer, address, medical_card_number)
VALUES('NIAMH','20 SYCAMOUR ROAD',134589);

INSERT INTO card_info(name_customer, address, medical_card_number)
VALUES('JORDAN','28 FITZROY AVE',134592);




INSERT INTO drug_book(drug_description,drug_dosage, name_customer)
VALUES('FOR HEADACHES',1,'JOE');

INSERT INTO drug_book(drug_description,drug_dosage, name_customer)
VALUES('FOR SOAR THROATS',1,'NIAMH');

INSERT INTO drug_book(drug_description,drug_dosage, name_customer)
VALUES('CONTRACEPTIVE',1,'JORDAN');




INSERT INTO SALES_BOOK(COST_A, stock_code, medical_card_number, quantity, prescription_number)
VALUES(12,123125,1345678,20,678);

INSERT INTO SALES_BOOK(COST_A, stock_code, medical_card_number, quantity, prescription_number)
VALUES(5,123127,134589,100,679);

INSERT INTO SALES_BOOK(COST_A, stock_code, medical_card_number, quantity, prescription_number)
VALUES(30,123576,134592,30,680);

INSERT INTO SALES_BOOK(COST_A, stock_code, medical_card_number, quantity, prescription_number)
VALUES(30,123730,NULL,30,NULL);




INSERT INTO non_drug_sales(DATE_SOLD,TIME_SOLD, cost_b, quantity, stock_code)
VALUES('4-March-2014',1200,20,1,123467);

INSERT INTO non_drug_sales(DATE_SOLD,TIME_SOLD, cost_b, quantity, stock_code)
VALUES('12-April-2015',1400,5,12,123980);

INSERT INTO non_drug_sales(DATE_SOLD,TIME_SOLD, cost_b, quantity, stock_code)
VALUES('23-Jan-2015',2000,15,1,123679);


SELECT * FROM non_drug_sales;

SELECT NAME_CUSTOMER FROM PRESCRIPTION_INFO;

SELECT ADDRESS
FROM PRESCRIPTION_INFO
ORDER BY unique_precription_number ;

SELECT NAME_CUSTOMER FROM PRESCRIPTION_INFO WHERE DAYS_TO_BE_TAKEN< 300;

SELECT STOCK_CODE FROM sales_book WHERE prescription_number IS NULL;

SELECT SUM(COST_A) FROM SALES_BOOK;

SELECT SUM(COST_A)
FROM sales_book
WHERE QUANTITY >20
GROUP BY COST_A;

SELECT SUM(COST_A)
FROM sales_book
WHERE QUANTITY >20
GROUP BY medical_card_number
HAVING SUM(cost_a)>10;

SELECT PRESCRIPTION_NUMBER FROM SALES_BOOK
UNION 
SELECT unique_precription_number FROM PRESCRIPTION_INFO;

SELECT PRESCRIPTION_NUMBER FROM SALES_BOOK
MINUS
SELECT unique_precription_number FROM PRESCRIPTION_INFO;

SELECT PRESCRIPTION_NUMBER FROM SALES_BOOK
INTERSECT
SELECT unique_precription_number FROM PRESCRIPTION_INFO;

SELECT STOCK_CODE, prescription_number FROM SALES_BOOK
INNER JOIN prescription_info
ON PRESCRIPTION_INFO.unique_precription_number=SALES_BOOK.prescription_number;

SELECT prescription_number FROM SALES_BOOK
INNER JOIN PHARMACY
USING (STOCK_CODE);

SELECT STOCK_CODE, prescription_number FROM SALES_BOOK 
INNER JOIN prescription_info
ON PRESCRIPTION_INFO.unique_precription_number=SALES_BOOK.prescription_number
WHERE cost_a>10;


SELECT NAME_CUSTOMER
FROM prescription_info
FULL OUTER JOIN sales_book
ON prescription_info.unique_precription_number=SALES_BOOK.prescription_number;




SELECT NAME_CUSTOMER FROM prescription_info 
WHERE unique_precription_number=
(SELECT prescription_number FROM SALES_BOOK WHERE prescription_number=680);+

SELECT BRAND_NAME, prescription_INFO.NAME_CUSTOMER FROM PHARMACY
INNER JOIN sales_book
USING (stock_code)
INNER JOIN PRESCRIPTION_INFO
ON SALES_BOOK.PRESCRIPTION_NUMBER=PRESCRIPTION_INFO.unique_precription_number;

GRANT select,insert, update ON pharmacy TO jward;
commit;

insert into jward.pharmacy(drug)
values('PENICILLIN');
COMMIT;

SELECT * FROM PHARMACY;


