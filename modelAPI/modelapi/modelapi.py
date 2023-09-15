from pymysql import connect
from datarecord.mysql_recorder_from_dir_with_id import MySQLRecorderFromDirWithID
from repository.dataset.mysql_dataset_repository import MySQLDatasetRepository
from dataprovide.Image_data_provider_by_many_id_from_mysql import ImageDataProviderByManyIdFromMySQL
from repository.database_manager import DatabaseManager
import sys, os

def main():
    db = DatabaseManager().get()
    for i in range(1, 100):
        # print("Record id {}".format(i))
        MySQLRecorderFromDirWithID(i, db).record()

    db.commit()

    img_ids = [2, 24, 5, 55, 62, 33, 23, 13]
    image_provider = ImageDataProviderByManyIdFromMySQL(img_ids, db)

    image_dtos = image_provider.get()

    for i in range(len(image_dtos)):
        image_dtos[i].image.save(os.path.dirname(sys.argv[0]) + "/temp_resource/%d.jpg" % i)

    db.close()


if __name__ == "__main__":
    main()