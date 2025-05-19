import os
import subprocess
import shutil

# 路径配置
src_base = "PIE_Preprocessed"
dst_base = "PIE_Preprocessed_g"
ghidra_headless = "ghidra_11.3.2_PUBLIC/support/analyzeHeadless"
script_path = "ghidra-headless-scripts"
p3_script = "p3.py"

# 需要处理的文件名
filenames = [
    "src_O0.o", "src_O1.o", "src_O2.o", "src_O3.o",
    "tgt_O0.o", "tgt_O1.o", "tgt_O2.o", "tgt_O3.o"
]

tmp_proj_path = "/tmp/ghidra_proj"

# 遍历所有子文件夹
for folder in sorted(os.listdir(src_base)):
    src_folder = os.path.join(src_base, folder)
    if not os.path.isdir(src_folder):
        continue

    # 清理旧的临时项目目录，避免残留冲突
    if os.path.exists(tmp_proj_path):
        shutil.rmtree(tmp_proj_path)
    os.makedirs(tmp_proj_path)

    print(f"Processing folder: {folder}")

    dst_folder = os.path.join(dst_base, folder)
    os.makedirs(dst_folder, exist_ok=True)

    # 使用时间戳或唯一标识项目名，避免冲突（可选）
    import time
    timestamp = int(time.time() * 1000)
    project_name = f"MyProj_{folder}_{timestamp}"

    for fname in filenames:
        o_file = os.path.join(src_folder, fname)
        if not os.path.isfile(o_file):
            print(f"  [!] Missing: {o_file}")
            continue

        # 输出文件名
        output_c = os.path.join(dst_folder, fname.replace(".o", "_decompiled.c"))

        cmd = [
            ghidra_headless,
            tmp_proj_path,
            project_name,
            "-import", o_file,
            "-scriptPath", script_path,
            "-postScript", p3_script, output_c
        ]

        print(f"  [+] Decompiling {fname} -> {output_c}")
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"  [!] Failed to decompile {fname}: {e}")
