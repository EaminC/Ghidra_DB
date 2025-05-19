import os
import json
import subprocess
import time

# Path configuration
data_folder = 'dataset'
output_folder = 'PIE_Preprocessed'

# Ensure output path exists
os.makedirs(output_folder, exist_ok=True)

def write_cpp_and_compile(folder, code, name):
    cpp_path = os.path.join(folder, f"{name}.cpp")
    with open(cpp_path, "w") as f:
        f.write(code)

    compiled_count = 0
    for opt in ["O0", "O1", "O2", "O3"]:
        obj_path = os.path.join(folder, f"{name}_{opt}.o")
        out_path = os.path.join(folder, f"{name}_{opt}.out")

        # Compile to .o
        compile_cmd = ["g++", f"-{opt}", "-c", cpp_path, "-o", obj_path]
        try:
            subprocess.run(compile_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"[Compilation Failed] {obj_path}")
            continue

        # Link to executable .out
        link_cmd = ["g++", obj_path, "-o", out_path]
        try:
            subprocess.run(link_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            compiled_count += 1
        except subprocess.CalledProcessError as e:
            print(f"[Linking Failed] {out_path}")
    
    return compiled_count

def preprocess_dataset():
    start_time = time.time()
    counter = 1
    total_samples = 0
    success_samples = 0
    total_files = 0

    print(f"[Start] Processing dataset from {data_folder}")

    for filename in os.listdir(data_folder):
        if not filename.endswith('.jsonl'):
            continue

        file_path = os.path.join(data_folder, filename)
        print(f"[Processing File] {filename}")
        file_samples = 0
        
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    print(f"[Parse Error] Sample {counter}")
                    counter += 1
                    continue

                sample_folder = os.path.join(output_folder, f"{counter:06d}")
                os.makedirs(sample_folder, exist_ok=True)

                # Save original jsonl line
                with open(os.path.join(sample_folder, "original.jsonl"), "w") as f:
                    f.write(line)

                src_code = data.get('src_code', '')
                tgt_code = data.get('tgt_code', '')

                if counter % 50 == 0:
                    print(f"[Progress] Processing sample {counter}")

                src_compiled = write_cpp_and_compile(sample_folder, src_code, "src")
                tgt_compiled = write_cpp_and_compile(sample_folder, tgt_code, "tgt")
                
                total_samples += 1
                file_samples += 1
                if src_compiled > 0 and tgt_compiled > 0:
                    success_samples += 1
                total_files += src_compiled + tgt_compiled

                counter += 1
        
        print(f"[File Complete] {filename} - Processed {file_samples} samples")

    elapsed_time = time.time() - start_time
    print(f"\n[Complete] Total processed: {total_samples} samples, Successful: {success_samples}")
    print(f"[Statistics] Generated {total_files} compiled files")
    print(f"[Time] Total time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    preprocess_dataset() 