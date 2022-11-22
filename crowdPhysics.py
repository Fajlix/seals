import numpy as np


# Found on https://www.researchgate.net/publication/334584008_Experiment_Calibrated_Simulation_Modeling_of_Crowding_Forces_in_High_Density_Crowd
def psychological_range(individual_local_crowd_density, comfort_density, safety_density, breathing_density, velocity,
                        reaction_time, sqeezing_amount, step_length):
    if individual_local_crowd_density <= comfort_density:
        return velocity * reaction_time + 2 * step_length
    elif individual_local_crowd_density <= safety_density:
        return velocity * reaction_time + step_length
    elif individual_local_crowd_density <= breathing_density:
        return max(velocity * reaction_time, sqeezing_amount)
    else:
        return sqeezing_amount


def crowd_density_for_agent(agent_area, distance_to_closest_agent, overlapping_area, radius_limb):
    if overlapping_area == 0:
        return 1 / (agent_area * np.power(1 + distance_to_closest_agent / radius_limb, 2))
    else:
        return 1 / (agent_area - overlapping_area)
