def process_invoice(net, gross):
    if net > gross:
        raise ValueError('Net value should be lower or equal to gross value.')
    else:
        print(f'Processing invoice: net={net}; gross={gross}')


def end_of_month():
    net_value = 1230
    gross_value = 10000

    try:
        process_invoice(net_value, gross_value)
    except ValueError as e:
        print(f'The values on invoice are incorrect: {e}')
        raise ValueError('Error when processing invoices') from e
    except Exception as e:
        print(f'Error processing invoice: {e}')
        raise Exception('General error when processing invoices')


end_of_month()
