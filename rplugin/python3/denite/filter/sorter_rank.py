# For backward compatibility
from denite.filter.sorter.rank import Filter as Base


class Filter(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = self.name.replace('/', '_')
