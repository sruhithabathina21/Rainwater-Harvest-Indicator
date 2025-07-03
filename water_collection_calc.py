def calculate_water_volume(rainfall_mm, rooftop_area_m2):
    """
    Estimate rainwater collected in Litres.
    1 mm rain on 1 m² = 1 litre. Assume 90% efficiency.
    """
    return rainfall_mm * rooftop_area_m2 * 0.9

if __name__ == "__main__":
    print("💧 Water Collection Estimator 💧")
    rainfall = float(input("Enter today's rainfall (mm): "))
    area = float(input("Enter rooftop area (m²): "))
    volume = calculate_water_volume(rainfall, area)
    print(f"Estimated water you can collect: {volume:.2f} Litres")
