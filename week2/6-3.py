# --------------------------------------------------------------------------------------

# class Student:
#     def __init__(self, name, student_id, grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade
#
#     def introduce(self):
#         print(f"안녕하세요, {self.grade}학년 {self.name}입니다. (학번 : {self.student_id})")
#
# student = Student("정민","2018",2)
# student.introduce()

# --------------------------------------------------------------------------------------

# class Bank:
#     def __init__(self, owner, balace):
#         self.owner = owner
#         self.balace = balace
#
#     def deposit(self, amount):
#         print(f"기존 잔액 : {self.balace}")
#         self.balace += amount
#         print(f"입금액 : {amount}, 현재 잔액 : {self.balace}\n")
#
#     def withdraw(self, amount):
#         print(f"기존 잔액 : {self.balace}")
#         self.balace -= amount
#         print(f"출금액 : {amount}, 현재 잔액 : {self.balace}\n")
#
#     def get_dalance(self):
#         print(f"잔액은 : {self.balace}")
#         return self.balace
#
# bank = Bank("정민",10000000)
# bank.deposit(20000000)
# bank.withdraw(40000000)
# bank.get_dalance()

# --------------------------------------------------------------------------------------

# class TodoList:
#     def __init__(self):
#         self.task = []
#
#     def add_task(self,new_task):
#         print(f"할일 추가 : {new_task}")
#         self.task.append(new_task)
#         print(f"현재 할일 :{self.task}")
#
#     def complete_task(self,new_task):
#         print(f"할일 완료 : {new_task}")
#         self.task.remove(new_task)
#         print(f"남은 할일 :{self.task}")
#
#     def show_task(self):
#         print(f"현재 남은 할일이 궁금하다고? : {self.task}")
#
# todo_list = TodoList()
# todo_list.add_task("집가고싶다")
# todo_list.add_task("파이썬 공부")
# todo_list.complete_task("파이썬 공부")
# todo_list.show_task()

# --------------------------------------------------------------------------------------

# import dataclasses
#
# @dataclasses.dataclass
# class DatabaseConfig:
#     host: str
#     port: int
#     username: str
#     password: str
#     database: str
#     timeout: int = 30
#     pool_size: int = 5
#
# config = DatabaseConfig("localhost",8080,"jm","jmpw","database")
# print(config)

# --------------------------------------------------------------------------------------

class EC2Instance:
    def __init__(self, instance_id, name, status = "stopped"):
        self.instance_id = instance_id
        self.name = name
        self.status = status

    def start(self):
        self.status = "running"

    def stop(self):
        self.status = "stopped"

class EC2Manager:
    def __init__(self):
        self.instances = []

    def add_instance(self,instance):
        self.instances.append(instance)
        print(f"추가 인스턴스 : {self.instances}")

    def start_all(self):
        for i in self.instances:
            i.start()

    def stop_all(self):
        for i in self.instances:
            i.stop()

    def get_running_count(self):
        count = 0
        for instance in self.instances:
            if instance.status == "running":
                count += 1
        return count

web = EC2Instance("i-001", "web-server")
db = EC2Instance("i-002", "db-server")
cache = EC2Instance("i-003", "cache-server")

# 매니저에 등록
manager = EC2Manager()
manager.add_instance(web)
manager.add_instance(db)
manager.add_instance(cache)

# 모두 시작
manager.start_all()
print(manager.get_running_count())  # 3

# 일부 중지
db.stop()
print(manager.get_running_count())  # 2