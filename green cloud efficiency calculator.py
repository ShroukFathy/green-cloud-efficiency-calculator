def calculate_energy_usage(servers, power_per_server, hours_per_day):
    return servers * power_per_server * hours_per_day / 1000  # kWh

def calculate_co2_emissions(energy_kwh):
    return energy_kwh * 0.475  # kg CO2

def simulate_green_efficiency():
    print("🌿 Green Cloud Efficiency Simulator")
    
    servers_before = int(input("Enter number of servers (before virtualization): "))
    servers_after = int(input("Enter number of servers (after virtualization): "))
    power_per_server = float(input("Enter average power usage per server (watts): "))
    hours_per_day = float(input("Enter hours of operation per day: "))
    
    energy_before = calculate_energy_usage(servers_before, power_per_server, hours_per_day)
    energy_after = calculate_energy_usage(servers_after, power_per_server, hours_per_day)

    co2_before = calculate_co2_emissions(energy_before)
    co2_after = calculate_co2_emissions(energy_after)
    
    savings_kwh = energy_before - energy_after
    savings_co2 = co2_before - co2_after
    
    print("\n📊 Results:")
    print(f"Energy before: {energy_before:.2f} kWh")
    print(f"Energy after: {energy_after:.2f} kWh")
    print(f"Carbon footprint reduced: {savings_co2:.2f} kg CO₂")
    print(f"Estimated cost savings: ${savings_kwh * 0.12:.2f}")

if __name__ == "__main__":
    simulate_green_efficiency()
