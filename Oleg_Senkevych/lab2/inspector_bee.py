class InspectorBee:
    """
       A class representing an inspector bee, which evaluates the quality of each food source
       and sends bees to collect them based on their quality.

       Attributes:
           None
    """
    def send_bees(self, sources, bees, hive):
        """
               Sends employed bees to gather food from the highest-quality sources.

               Args:
                   sources (list of FoodSource objects): The list of food sources to evaluate.
                   bees (list of EmployedBee objects): The list of employed bees available to collect food.
                   hive (Hive object): The hive from which the bees are departing.

               Returns:
                   None
        """
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