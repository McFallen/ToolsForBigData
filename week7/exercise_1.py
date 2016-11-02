from mrjob.job import MRJob

class exercise1(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    exercise1.run()