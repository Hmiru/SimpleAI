from pymysql.connections import Connection
from pymysql import connect
from repository.dataset.mysql_dataset_repository import MySQLDatasetRepository, DataDTO

def main():
    db = connect(host = "mysql", user = "root", password = "1234", database = "model_db")
    repo = MySQLDatasetRepository(db)
    dto1 = DataDTO("TEST1", "0/test1.jpg")
    dto2 = DataDTO("TEST2", "0/test2.jpg")
    dto3 = DataDTO("TEST3", "0/test3.jpg")
    dto4 = DataDTO("TEST4", "0/test4.jpg")
    dto5 = DataDTO("TEST1", "0/test5.jpg")
    dto6 = DataDTO("TEST2", "0/test6.jpg")
    dto7 = DataDTO("TEST3", "0/test7.jpg")
    dto8 = DataDTO("TEST4", "0/test8.jpg")

    repo.insert(dto1)
    repo.insert_list([dto2, dto3, dto4, dto5, dto6, dto7, dto8])

    db.commit()

    dto_get = repo.get(1)

    print("dto_Get")
    print(dto_get)

    dto_get_list = repo.get_list([1,2,3])

    print("dto get_list")
    for i in dto_get_list:
        print(i)

    dto_get_all = repo.get_all()
    print("dto get_all")
    for i in dto_get_all:
        print(i)

    dto_get_with_label = repo.get_all_with_label("TEST1")
    print("dto get_all_with_label")
    for i in dto_get_with_label:
        print(i)

    dto_deleted = repo.delete(5)
    print("DELETE")
    print(dto_deleted)
    print("REMAIN")
    dto_remain = repo.get_all()
    for i in dto_remain:
        print(i)

    dto_deleted_list = repo.delete_list([6,7,8])
    print("DELETE LISt")
    for i in dto_deleted_list:
        print(i)
    print("REMAIN")
    dto_remain = repo.get_all()
    for i in dto_remain:
        print(i)

    dto_before_update = repo.update(1, DataDTO("TESTTEST", "0/test1.jpg"))
    repo.commit()
    print("before edited")
    print(dto_before_update)
    print("After update")
    print(repo.get(1))

if __name__ == "__main__":
    main()