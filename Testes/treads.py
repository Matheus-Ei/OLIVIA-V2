import asyncio
import tkinter as tk

async def async_mainloop():
    root = tk.Tk()
    # Defina sua interface gráfica aqui
    while True:
        root.update()  # Atualiza a interface gráfica
        await asyncio.sleep(0.1)


async def other_async_task():
    # Outras tarefas assíncronas
    while True:
        print("Outra tarefa assíncrona")
        await asyncio.sleep(1)



async def main():
    await asyncio.gather(async_mainloop(), other_async_task())


asyncio.run(main())
