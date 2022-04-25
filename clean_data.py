import json

with open('yelp_dataset-2/yelp_academic_dataset_business.json', mode="r", encoding="utf-8") as file_read:
    with open('yelp_academic_dataset_business_clean.json', "w+") as file_write:
        try:
            while True:
                line_data = file_read.readline()

                if line_data:
                    data = json.loads(line_data)
                else:
                    break

                business_id = data['business_id']
                name = data['name']
                stars = data['stars']
                review_count = data['review_count']
                city = data['city']
                state = data['state']

                temp_dict = {"business_id": business_id, "name": name, "stars": stars, "review_count": review_count, "city": city, "state": state}

                json.dump(temp_dict,file_write)
                file_write.write("\n")

        except Exception as e:
            print(e)
            file_read.close()
            file_write.close()




with open('yelp_dataset-2/yelp_academic_dataset_review.json', mode="r", encoding="utf-8") as file_read:
    with open('yelp_academic_dataset_review_clean.json', "w+") as file_write:
        try:
            while True:
                line_data = file_read.readline()

                if line_data:
                    data = json.loads(line_data)
                else:
                    break

                review_id = data['review_id']
                user_id = data['user_id']
                business_id = data['business_id']
                stars = data['stars']

                temp_dict = {"review_id": review_id, "user_id": user_id, "business_id": business_id, "stars": stars}

                json.dump(temp_dict,file_write)
                file_write.write("\n")

        except Exception as e:
            print(e)
            file_read.close()
            file_write.close()




with open('yelp_dataset-2/yelp_academic_dataset_user.json', mode="r", encoding="utf-8") as file_read:
    with open('yelp_academic_dataset_user_clean.json', "w+") as file_write:
        try:
            while True:
                line_data = file_read.readline()

                if line_data:
                    data = json.loads(line_data)
                else:
                    break

                user_id = data['user_id']
                name = data['name']
                review_count = data['review_count']

                temp_dict = {"user_id": user_id, "name": name, "review_count": review_count}

                json.dump(temp_dict,file_write)
                file_write.write("\n")

        except Exception as e:
            print(e)
            file_read.close()
            file_write.close()