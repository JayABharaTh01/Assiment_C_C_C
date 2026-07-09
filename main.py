from data_pipeline.data_read import DataReader


def main():

    reader = DataReader("data")

    documents = reader.read_all_files()

    for doc in documents:

        print("=" * 60)

        print(f"File Name : {doc['filename']}")
        print(f"File Type : {doc['filetype']}")

        print("-" * 60)

        print(doc["content"][:500])

        print()


if __name__ == "__main__":
    main()