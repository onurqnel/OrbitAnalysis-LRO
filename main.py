import spiceypy as spice

def main():
    # Load the meta-kernel
    spice.furnsh("kernels/meta_kernel.tm")
    print("Kernels loaded successfully!")
    
    # Convert a UTC time string to ephemeris time.
    et = spice.utc2et("2020-01-01T00:00:00")
    print("Ephemeris time for 2020-01-01T00:00:00 is:", et)
    
    # Clear kernels 
    spice.kclear()

if __name__ == "__main__":
    main()
