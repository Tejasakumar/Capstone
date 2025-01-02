import r2pipe

def convert_to_assembly(exe_path, output_path):
    try:
        # Open the executable with Radare2
        r2 = r2pipe.open(exe_path)

        # Analyze the binary
        r2.cmd("aaa")

        # Disassemble the entire binary
        assembly_code = r2.cmd("pD")

        # Filter out non-assembly lines
        assembly_lines = []
        for line in assembly_code.splitlines():
            if line.strip() and not line.startswith(";"):
                assembly_lines.append(line)

        # Write the assembly code to the output file
        with open(output_path, "w") as f:
            f.write("\n".join(assembly_lines))

        print(f"Assembly code saved to {output_path}")

        # Close Radare2
        r2.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    exe_path = "mylex.exe"
    output_path = "output"
    convert_to_assembly(exe_path, output_path)
