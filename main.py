import spiceypy as spice
import numpy as np

def main():
    # Load all necessary kernels via the meta-kernel.
    spice.furnsh("kernels/meta_kernel.tm")
    print("Kernels loaded successfully!")
    
    # Convert a UTC time string (within the SPK's coverage) to ephemeris time.
    et = spice.utc2et("2024-06-20T00:00:00")
    print("Ephemeris time for 2024-06-20T00:00:00 is:", et)
    
    # Retrieve the state vector of the spacecraft relative to the Moon,
    # expressed in the inertial J2000 frame. 
    # Using an inertial frame avoids needing Moon-fixed orientation data.
    state, lt = spice.spkezr("LRO", et, "J2000", "NONE", "MOON")
    
    # Extract position (km) and velocity (km/s) from the state vector.
    pos_km = state[0:3]
    vel_kmps = state[3:6]
    
    # Convert position and velocity to SI units (meters and m/s).
    pos_m = np.array(pos_km) * 1000.0
    vel_mps = np.array(vel_kmps) * 1000.0
    
    # Calculate the orbital radius (distance from the Moon's center) and speed.
    r = np.linalg.norm(pos_m)
    v = np.linalg.norm(vel_mps)
    
    print(f"Orbital radius (r): {r:.2f} m")
    print(f"Orbital speed (v): {v:.2f} m/s")
    
    # Gravitational constant in SI units (m^3 kg^-1 s^-2)
    G = 6.67430e-11
    
    # Calculate the Moon's mass using the formula for a circular orbit:
    # Moon's Mass = (r * v^2) / G
    mass_moon = (r * v**2) / G
    print(f"Calculated Moon's mass: {mass_moon:.3e} kg")
    
    # Clear loaded kernels.
    spice.kclear()

if __name__ == "__main__":
    main()
