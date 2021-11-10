class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        current_cat_id = category.id
        for ctgr in self.categories:
            if ctgr.id == current_cat_id:
                return
        self.categories.append(category)

    def add_topic(self, topic):
        current_tpc_id = topic.id
        for tpc in self.topics:
            if tpc.id == current_tpc_id:
                return
        self.topics.append(topic)

    def add_document(self, document):
        current_doc_id = document.id
        for doc in self.documents:
            if doc.id == current_doc_id:
                return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for ctgry in self.categories:
            if ctgry.id == category_id:
                ctgry.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        for doc in self.documents:
            if doc.id == document_id:
                doc.file_name = new_file_name

    def delete_category(self, category_id):
        for ctgry in self.categories:
            if ctgry.id == category_id:
                self.categories.remove(ctgry)

    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                self.documents.remove(doc)

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc

    def __repr__(self):
        result = ''
        for doc in self.documents:
            result += str(doc) + '\n'
        return result
