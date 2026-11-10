"""demo-x 入口：连本地 Ollama 验证方案可行性"""
import ollama

def main():
    r = ollama.chat(
        model="qwen3:32b-q8_0",
        messages=[{"role": "user", "content": "用一句话证明本地模型可用，并列出你能读到的上级KB文件"}],
    )
    print(r.message.content)

if __name__ == "__main__":
    main()
