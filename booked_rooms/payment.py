from typing import Protocol


class IPaymentService(Protocol):
    starts: str

    def charge(self, card_number: int, card_date: str, csv: int) -> bool:
        raise NotImplementedError


class VisaPayment(IPaymentService):
    starts = "8600"

    def charge(self, card_number: int, card_date: str, csv: int) -> bool:
        return True


class MasterCardPayment(IPaymentService):
    starts = "9860"

    def charge(self, card_number: int, card_date: str, csv: int) -> bool:
        return True


list_services = [VisaPayment(), MasterCardPayment()]


class GetPaymentServiceImpl:
    def __init__(self, payment_services: list[IPaymentService]):
        self.payment_services = payment_services

    def __call__(self, starts_with: str) -> IPaymentService:
        for service in self.payment_services:
            if starts_with == service.starts:
                return service
        else:
            return self.payment_services[0]


def payment_international(card_number: int, card_date: str, csv: int) -> bool:
    payment_service = GetPaymentServiceImpl(payment_services=list_services)
    service = payment_service(starts_with=str(card_number)[:4])
    return service.charge(card_number=card_number, card_date=card_date, csv=csv)
