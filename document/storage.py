class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []
    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)
    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)
    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)
    def edit_category(self, category_id, new_name):
        if self.categories:
            category_id_change = [c for c in self.categories if c.id == category_id][0]
            if category_id_change:
                category_id_change.edit(new_name)
    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        if self.topics:
            topic_id_change = [c for c in self.topics if c.id == topic_id][0]
            if topic_id_change:
                topic_id_change.edit(new_topic, new_storage_folder)
    def edit_document(self, document_id, new_file_name):
        if self.documents:
            document_id_change = [d for d in self.documents if d.id == document_id][0]
            if document_id_change:
                document_id_change.edit(new_file_name)
    def delete_category(self, category_id):
        if self.categories:
            category_id_change = [c for c in self.categories if c.id == category_id][0]
            if category_id_change:
                self.categories.remove(category_id_change)
    def delete_topic(self, topic_id):
        if self.topics:
            topic_id_change = [c for c in self.topics if c.id == topic_id][0]
            if topic_id_change:
                self.topics.remove(topic_id_change)
    def delete_document(self, document_id):
        if self.documents:
            document_id_change = [d for d in self.documents if d.id == document_id][0]
            if document_id_change:
                self.documents.remove(document_id_change)
    def get_document(self, document_id):
        document_id_change = [d for d in self.documents if d.id == document_id][0]
        return document_id_change
    def __repr__(self):
        result = '\n'.join([repr(c) for c in self.documents])
        return result