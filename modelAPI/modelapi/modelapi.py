import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pymysql import connect
from datarecord.mysql_recorder_from_dir_with_id import MySQLRecorderFromDirWithID
from repository.dataset.mysql_dataset_repository import MySQLDatasetRepository

def main():
    db = connect(host = "mysql", user = "root", password = "1234", database = "model_db")
    for i in range(1, 25001):
        # print("Record id {}".format(i))
        MySQLRecorderFromDirWithID(i, db).record()

    db.commit()

    repo = MySQLDatasetRepository(db)

    print("LABEL: Summer_Night")
    dtos = repo.get_all_with_label("Summer_Night")

    for i in dtos:
        print(i)

    print("All datas : %i" % repo.count())
    print("Summer_Morning datas : %i" % repo.count_label("Summer_Morning"))
    print("Summer_Afternoon datas : %i" % repo.count_label("Summer_Afternoon"))
    print("Summer_Night datas : %i" % repo.count_label("Summer_Night"))


if __name__ == "__main__":
    main()