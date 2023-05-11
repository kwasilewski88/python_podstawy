# Rozważ klasę Case, która będzie inicjalizowana wraz z poniższymi danymi:
#
# first_case = {
#     ‘name’: ‘first_case’,
#     ‘created_task’: ‘2021-10-26T19:48:12+00:00’,
#     ‘end_task’: None
# }
#
# second_case = {
#     ‘name’: ‘second_case’,
#     ‘created_task’: ‘2021-09-26T19:48:12+00:00’,
#     ‘end_task’: ‘2021-10-26T19:48:12+00:00’
# }
#
# Klasa Case ma zawierać metodę retrieve_seconds,
# która zwracać będzie różnicę czasową między end_task a created_task podaną w sekundach.
#
# UWAGA
# 1. Wartość None przypisana do klucza end_task oznacza, że task jeszcze trwa.
# 2. Zwróć uwagę na to, iż retrieve_seconds możemy wywoływać wielokrotnie
import datetime


class Case:
    def __init__(self, name, created_task, end_task):
        self.name = name
        self.created_task = created_task
        self.end_task = end_task

    def retrieve_seconds(self):
        if self.end_task is None:
            end_task = datetime.datetime.now(datetime.timezone.utc).astimezone()
        else:
            end_task = datetime.datetime.strptime(self.end_task, '%Y-%m-%dT%H:%M:%S%z')
        diff = end_task - datetime.datetime.strptime(self.created_task, '%Y-%m-%dT%H:%M:%S%z')
        return diff.total_seconds()


first_case = Case('first_case', "2021-10-26T19:48:12+00:00", None)

print(first_case.retrieve_seconds())
print(first_case.retrieve_seconds())

second_case = Case('second_case', "2021-09-26T19:48:12+00:00", "2021-10-26T19:48:12+00:00")

print(second_case.retrieve_seconds())
print(second_case.retrieve_seconds())
