import traceback
from openai import OpenAI

SYSTEM_PROMPT = """
你是一名的专业的字幕翻译工作者。现在你的任务是帮助用户将字幕文本从一种语言翻译到另一种语言，要求符合目标语言的表达习惯，表达专业地道，语法正确；保留常用的专业名词以及用户指定的专业词汇。只返回翻译后的文本，不能包含任何其它的内容。
""".strip()

CUSTOM_PROMPT = """
{head}

字幕文本：{text}

翻译：
""".strip()


def translate_text(
    text: str,
    tar_lan: str,
    src_lan: str = None,
    special_vocabs: list[str] = [],
    model: str = "Qwen/Qwen2.5-72B-Instruct",
    api_key: str = None,
    base_url: str = None,
):
    client = OpenAI(api_key=api_key, base_url=base_url)

    head = ""
    if src_lan:
        head += f"将字幕文本从`{src_lan}`翻译成`{tar_lan}`"
    else:
        head += f"将字幕文本翻译成`{tar_lan}`"
    if special_vocabs:
        special_vocabs = " - " + "\n - ".join(special_vocabs)
        head += f"，同时保留以下词汇（如果有的话）：\n{special_vocabs}"

    content = CUSTOM_PROMPT.format(head=head, text=text)

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": content},
            ],
            temperature=0.0,
            stream=False,
        )
        return resp.choices[0].message.content.lstrip("翻译：")

    except Exception as e:
        traceback.print_exception(e)

        return text


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    text = "well we nice acted a frog"
    src_lan = "English"
    tar_lan = "中文"
    model = "Qwen/Qwen2.5-72B-Instruct"
    special_vocabs = ["frog"]
    resp = translate_text(
        text=text,
        tar_lan=tar_lan,
        src_lan=src_lan,
        special_vocabs=special_vocabs,
        model=model,
        api_key=os.environ.get("API_KEY"),
        base_url=os.environ.get("BASE_URL"),
    )
    print(resp)
