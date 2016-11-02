from mrjob.job import MRJob
from mrjob.step import MRStep
class exercise2(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.euler_reducer)
                ]


    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, key, values):
        yield None, sum(values) % 2 == 0

    @staticmethod
    def is_list_true(sel):
        is_true = True
        for x in sel:
            is_true = is_true and x
        return is_true

    def euler_reducer(self, _, values):
        yield "Does an euler tour exist?", self.is_list_true(values)


if __name__ == "__main__":
    exercise2.run()