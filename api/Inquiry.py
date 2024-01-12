from fastapi import APIRouter, Depends
from model import InqBalanceRequest
from model import InqBalanceResponse
from db import get_db
from sqlalchemy.orm import Session
import logging
import logging.config
import cx_Oracle

router = APIRouter()

@router.post("/payment", response_model=list[InqBalanceResponse.Data])
def inquiry(inq: InqBalanceRequest.param, db: Session = Depends(get_db)):
    cur = db.cursor()
    l_cur = cur.var(cx_Oracle.CURSOR)
    cur.callproc('sp_rpt_autodebit_api',[inq.fromDate, inq.toDate, inq.providerCode, "success", l_cur])
    results = l_cur.getvalue().fetchall()
    items = []
    for x in results:
        items.append({"agreement_no": x[0], 
                      "customer_name": x[1], 
                      "mobile_no": x[2], 
                      "transfer_amount": x[3], 
                      "term": x[4], 
                      "start_date": x[5], 
                      "stop_date": x[6],
                      "date_process": x[7],
                      "ccy": x[8],
                      "company": x[9],
                      "ref_no": x[10],
                      "response_code": x[11],
                      "response_desc": x[12],
                      "company_account_number": x[13],
                      "company_account_name": x[14],
                      "company_detail_1": x[15],
                      "company_detail_2": x[16],
                      "company_detail_3": x[17]})
    return items
  