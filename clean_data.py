import json

# Opening JSON file
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

                temp_dict = {"business_id": business_id, "name": name, "stars": stars, "review_count": review_count}

                json.dump(temp_dict,file_write)
                file_write.write("\n")

        except Exception as e:
            print(e)
            file_read.close()
            file_write.close()