from mdules import Storage

class ProcessLine:

    def __init__(self, vcf_line):
        self.vcf_line = vcf_line
        self.sample_names = []
        if self.vcf_line.startswith("#C"):
            self.samples = []
            self.sample_names = self.vcf_line.split()[9:]
            self.storage = Storage.AllSamples()
            for sample in self.sample_names:
                new_sample = Storage.Sample(sample_name=sample)
                self.samples.append(new_sample)



    def