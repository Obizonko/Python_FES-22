class InspectorBee:
    def send_bees(self, sources, bees, hive):
        sources_quality = []
        for source in sources:
            quality = source.quality(bees, hive)
            print(source.location, ' ', quality)
            sources_quality.append((source, quality))
        sorted_sources = sorted(
            sources_quality,
            key=lambda x: x[1],
            reverse=True)
        for i in range(min(len(sorted_sources), len(bees))):
            bees[i].fly(sorted_sources[i][0])