def bytes_to_pdf(buffer: bytes) -> str:
    with open('tmp.pdf', 'wb') as f:
        f.write(buffer)
    return f.name
