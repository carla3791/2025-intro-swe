from behave import given, when, then
from app.db import load_books
from app.embeddings import build_index, embed_query

@given('the BookSeeker database is loaded')
def step_impl(context):
    context.books = load_books()
    context.index, _ = build_index(context.books)

@when('I search for "{query}"')
def step_impl(context, query):
    qvec = embed_query(query)
    D, I = context.index.search(qvec, 3)
    context.result_idx = I[0][0]

@then('the top result should contain "{title}"')
def step_impl(context, title):
    idx = context.result_idx
    assert title in context.books[idx]["title"]
