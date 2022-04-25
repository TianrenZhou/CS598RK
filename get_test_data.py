import json

with open('yelp_academic_dataset_business_clean.json', mode="r", encoding="utf-8") as file_read:
    with open('testset_business_@_CA.json', "w+") as file_write:
        try:
            while True:
                line_data = file_read.readline()

                if line_data:
                    data = json.loads(line_data)

                    if data['state'] == 'CA':
                        data = json.loads(line_data)

                        business_id = data['business_id']
                        name = data['name']
                        stars = data['stars']
                        review_count = data['review_count']
                        city = data['city']

                        temp_dict = {"business_id": business_id, "name": name, "stars": stars, "review_count": review_count, "city": city}

                        json.dump(temp_dict, file_write)
                        file_write.write("\n")

                    else:
                        continue

                else:
                    break


        except Exception as e:
            print(e)
            file_read.close()
            file_write.close()





business_list = []
user_list = []

with open('testset_business_@_CA.json', mode="r", encoding="utf-8") as file_read_business:
    while True:
        line_data = file_read_business.readline()

        if line_data:
            business_id = json.loads(line_data)['business_id']
            business_list.append(business_id)
        else:
            break

with open('yelp_academic_dataset_review_clean.json', mode="r", encoding="utf-8") as file_read_review:
    with open('testset_review_@_CA.json', "w+") as file_write:
        try:
            while True:
                line_data = file_read_review.readline()

                if line_data:
                    data = json.loads(line_data)

                    if data['business_id'] in business_list:
                        review_id = data['review_id']
                        user_id = data['user_id']
                        business_id = data['business_id']
                        stars = data['stars']

                        user_list.append(user_id)

                        temp_dict = {"review_id": review_id, "user_id": user_id, "business_id": business_id, "stars": stars}

                        json.dump(temp_dict, file_write)
                        file_write.write("\n")

                else:
                    break

        except Exception as e:
            print(e)
            file_read_review.close()
            file_write.close()



user_set = set(user_list)


# with open('testset_review_@_CA.json', mode="r", encoding="utf-8") as file_read_business:

with open('yelp_academic_dataset_user_clean.json', mode="r", encoding="utf-8") as file_read_user:
    with open('testset_user_@_CA.json', "w+") as file_write:
        try:
            while True:
                line_data = file_read_user.readline()

                if line_data:
                    data = json.loads(line_data)

                    if data['user_id'] in user_set:
                        user_id = data['user_id']
                        name = data['name']
                        review_count = data['review_count']

                        temp_dict = {"user_id": user_id, "name": name, "review_count": review_count}

                        json.dump(temp_dict, file_write)
                        file_write.write("\n")

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
            file_read_user.close()
            file_write.close()

