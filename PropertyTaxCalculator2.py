# HMO Deal Calc 2022
# ------------------
# Property of Astro Tech LLC
# For licensing contact us at AstroTechLLC.com

from tkinter import *

root = Tk()
root.title('HMO Deal Calculator')
root.geometry("1400x850")
mainframe = Frame(root)
mainframe.pack(fill="both")

def reset():
    #Reset of all entries, re-disable fields that don't require user input
    # Reset purchase price input
    purchase_price_entry.delete(0, END)
    
    # Reset mortgage ltv input
    mortgage_ltv_entry.delete(0, END)
    
    # Reset mortgage amt output
    mortgage_amount_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    mortgage_amount_entry.delete(0, END)
    mortgage_amount_entry.grid(row=3, column=1)
    
    # Reset deposit amt output
    deposit_amount_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    deposit_amount_entry.delete(0, END)
    deposit_amount_entry.grid(row=4, column=1)
    
    # Reset stamp duty output
    stamp_duty_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    stamp_duty_entry.delete(0, END)
    stamp_duty_entry.grid(row=5, column=1)
    
    # Reset refurb costs input
    refurb_costs_entry.delete(0, END)

    # Reset mortgage brokerage costs input
    mortgage_broker_costs_entry.delete(0, END)

    # Reset survey+vat costs input
    survey_vat_costs_entry.delete(0, END)

    # Reset legal costs input
    legal_costs_entry.delete(0, END)

    # Reset total capital employed output
    total_capital_employed_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    total_capital_employed_entry.delete(0, END)
    total_capital_employed_entry.grid(row=10, column=1, pady=20)

    # Reset total purchase costs output
    total_purchase_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    total_purchase_costs_entry.delete(0, END)
    total_purchase_costs_entry.grid(row=11, column=1)

    # Reset num lettable rooms input
    num_lettable_rooms_entry.delete(0, END)

    # Reset num avg room rental input
    avg_room_rental_entry.delete(0, END)

    # Reset monthly costs input
    monthly_costs_entry.delete(0, END)

    # Reset monthly rent total output
    monthly_rent_total_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    monthly_rent_total_entry.delete(0, END)
    monthly_rent_total_entry.grid(row=4, column=3, pady=20)

    # Reset monthly rent total output
    monthly_revenue_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    monthly_revenue_entry.delete(0, END)
    monthly_revenue_entry.grid(row=5, column=3)

    # Reset bills per room input
    bills_per_room_entry.delete(0, END)

    # Reset total bills output
    total_bills_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    total_bills_entry.delete(0, END)
    total_bills_entry.grid(row=2, column=5)

    # Reset management % input
    management_fee_entry.delete(0, END)

    # Reset management costs output
    management_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    management_costs_entry.delete(0, END)
    management_costs_entry.grid(row=4, column=5)

    # Reset insurance input
    insurance_entry.delete(0, END)

    # Reset cleaning input
    cleaning_entry.delete(0, END)

    # Reset void percentage input
    void_percentage_entry.delete(0, END)

    # Reset void cost output
    void_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    void_costs_entry.delete(0, END)
    void_costs_entry.grid(row=8, column=5)

    # Reset maintenance percentage input
    maintenance_percentage_entry.delete(0, END)

    # Reset maintenance costs output
    maintenance_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    maintenance_costs_entry.delete(0, END)
    maintenance_costs_entry.grid(row=10, column=5)

    # Reset mortgage rate input
    mortgage_rate_entry.delete(0, END)

    # Reset mortgage costs output
    mortgage_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    mortgage_costs_entry.delete(0, END)
    mortgage_costs_entry.grid(row=12, column=5, pady=20)

    # Reset total expenditure output
    total_expenditure_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    total_expenditure_entry.delete(0, END)
    total_expenditure_entry.grid(row=13, column=5)

    # Reset price per room output
    price_per_room_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    price_per_room_entry.delete(0, END)
    price_per_room_entry.grid(row=1, column=7)

    # Reset gross yield output
    gross_yield_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    gross_yield_entry.delete(0, END)
    gross_yield_entry.grid(row=2, column=7)

    # Reset net yield output
    net_yield_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    net_yield_entry.delete(0, END)
    net_yield_entry.grid(row=3, column=7)

    # Reset monthly gross revenue output
    monthly_gross_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    monthly_gross_entry.delete(0, END)
    monthly_gross_entry.grid(row=4, column=7)

    # Reset monthly net revenue output
    monthly_net_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    monthly_net_entry.delete(0, END)
    monthly_net_entry.grid(row=5, column=7)

    # Reset annual net revenue output
    annual_net_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    annual_net_entry.delete(0, END)
    annual_net_entry.grid(row=6, column=7)

    # Reset occupancy to break even output
    occupancy_break_even_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    occupancy_break_even_entry.delete(0, END)
    occupancy_break_even_entry.grid(row=7, column=7)

    # Reset return on capital employed output
    return_on_capital_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    return_on_capital_entry.delete(0, END)
    return_on_capital_entry.grid(row=8, column=7)
    
def format(var):
    var = var.replace(',','')
    var = float(var.replace('£',''))
    return var
    

def calculate():
    if purchase_price_entry.get() and mortgage_ltv_entry.get() and refurb_costs_entry.get() and mortgage_broker_costs_entry.get() and survey_vat_costs_entry.get() and legal_costs_entry.get() and num_lettable_rooms_entry.get() and avg_room_rental_entry.get() and monthly_costs_entry.get() and bills_per_room_entry.get() and management_fee_entry.get() and insurance_entry.get() and cleaning_entry.get() and void_percentage_entry.get() and maintenance_percentage_entry.get() and mortgage_rate_entry.get():
        
        # Purchase Column Calculations
        # Needs to grab updated value to redo calculations
 
        purchase_price = purchase_price_entry.get()
        purchase_price = format(purchase_price)

        mortgage_ltv_percentage = mortgage_ltv_entry.get()
        mortgage_ltv_percentage = float(mortgage_ltv_percentage.replace('%',''))
        mortgage_ltv = mortgage_ltv_percentage/100
        
        mortgage_total = purchase_price * mortgage_ltv
        mortgage_amount_entry = Entry(purchase_frame, font=("Helvetica", 10))
        mortgage_amount_entry.insert(0, f'£{mortgage_total:,.2f}')
        mortgage_amount_entry.grid(row=3, column=1)

        deposit = purchase_price - mortgage_total
        deposit_amount_entry = Entry(purchase_frame, font=("Helvetica", 10))
        deposit_amount_entry.insert(0, f'£{deposit:,.2f}')
        deposit_amount_entry.grid(row=4, column=1)
        
        # Calculate Stamp Duty (Provided By Tarkat)
        if purchase_price<=125000:
            stamp_duty = purchase_price*0.03
        elif purchase_price>125000 and purchase_price<=250000:
            taxUnderBracket = (125000*0.03)
            stamp_duty = taxUnderBracket + ((purchase_price-125000)*0.05)
        elif purchase_price>250000 and purchase_price<=925000:
            taxUnderBracket =(125000*0.03) + ((250000-125000)*0.05)
            stamp_duty = taxUnderBracket + ((purchase_price-250000)*0.08)
        elif purchase_price>925000 and purchase_price<=1500000:
            taxUnderBracket =(125000*0.03) + ((250000-125000)*0.05)+(675000*0.08)
            stamp_duty = taxUnderBracket + ((purchase_price-925000)*0.13)
        else:
            taxUnderBracket = (125000*0.03) + ((250000-125000)*0.05)+(675000*0.08)+((1500000-925000)*0.13)
            stamp_duty = taxUnderBracket + ((purchase_price-1500000)*0.15)

        # Format Stamp Duty Output
        stamp_duty_entry = Entry(purchase_frame, font=("Helvetica", 10))
        stamp_duty_entry.insert(0, f'£{stamp_duty:,.2f}')
        stamp_duty_entry.grid(row=5, column=1)
        
        # Format Purchase Price inputs
        purchase_price_entry.delete(0, END)
        purchase_price_entry.insert(0, f'£{purchase_price:,.2f}')

        # Format Mortgage LTV % inputs
        mortgage_ltv_entry.delete(0, END)
        mortgage_ltv_entry.insert(0, f'{mortgage_ltv_percentage}%')

        # Format Refurb Costs input
        refurb_costs = refurb_costs_entry.get()
        refurb_costs = refurb_costs.replace(',','')
        refurb_costs = float(refurb_costs.replace('£',''))
        refurb_costs_entry.delete(0, END)
        refurb_costs_entry.insert(0, f'£{refurb_costs:,.2f}')

        # Format Mortgage Brokerage input
        mortgage_brokerage = mortgage_broker_costs_entry.get()
        mortgage_brokerage = mortgage_brokerage.replace(',','')
        mortgage_brokerage = float(mortgage_brokerage.replace('£',''))
        mortgage_broker_costs_entry.delete(0, END)
        mortgage_broker_costs_entry.insert(0, f'£{mortgage_brokerage:,.2f}')

        # Format Survey inv VAT costs input
        survey_costs = survey_vat_costs_entry.get()
        survey_costs = survey_costs.replace(',','')
        survey_costs = float(survey_costs.replace('£',''))
        survey_vat_costs_entry.delete(0, END)
        survey_vat_costs_entry.insert(0, f'£{survey_costs:,.2f}')

        # Format Legal Costs input
        legal_costs = legal_costs_entry.get()
        legal_costs = legal_costs.replace(',','')
        legal_costs = float(legal_costs.replace('£',''))
        legal_costs_entry.delete(0, END)
        legal_costs_entry.insert(0, f'£{legal_costs:,.2f}')
        
        # Format Total Capital Employed output
        total_capital_employed = float(deposit + stamp_duty + refurb_costs + mortgage_brokerage + survey_costs + legal_costs)
        total_capital_employed_entry = Entry(purchase_frame, font=("Helvetica", 10))
        total_capital_employed_entry.delete(0, END)
        total_capital_employed_entry.insert(0, f'£{total_capital_employed:,.2f}')
        total_capital_employed_entry.grid(row=10, column=1, pady=20)

        # Format Total Purchase Cost output
        total_purchase_costs = float(purchase_price + stamp_duty + refurb_costs + mortgage_brokerage + survey_costs + legal_costs)
        total_purchase_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
        total_purchase_costs_entry.insert(0, f'£{total_purchase_costs:,.2f}')
        total_purchase_costs_entry.grid(row=11, column=1)

        # Monthly Revenue Column Calculations
        # Format # of lettable rooms input
        num_lettable_rooms = num_lettable_rooms_entry.get()
        num_lettable_rooms = float(num_lettable_rooms.replace(',',''))
        num_lettable_rooms_entry.delete(0, END)
        num_lettable_rooms_entry.insert(0, f'{num_lettable_rooms:,.0f}')

        # Format avg room rental input
        avg_room_rental = avg_room_rental_entry.get()
        avg_room_rental = avg_room_rental.replace(',','')
        avg_room_rental = float(avg_room_rental.replace('£',''))
        avg_room_rental_entry.delete(0, END)
        avg_room_rental_entry.insert(0, f'£{avg_room_rental:,.2f}')

        # Format monthly costs
        monthly_costs = monthly_costs_entry.get()
        monthly_costs = monthly_costs.replace(',','')
        monthly_costs = float(monthly_costs.replace('£',''))
        monthly_costs_entry.delete(0, END)
        monthly_costs_entry.insert(0, f'£{monthly_costs:,.2f}')

        # Format monthly rent total output
        monthly_rent_total = num_lettable_rooms * avg_room_rental
        monthly_rent_total_entry = Entry(purchase_frame, font=("Helvetica", 10))
        monthly_rent_total_entry.insert(0, f'£{monthly_rent_total:,.2f}')
        monthly_rent_total_entry.grid(row=4, column=3, pady=20)

        # Format monthly revenue output
        monthly_revenue = monthly_rent_total - monthly_costs
        monthly_revenue_entry = Entry(purchase_frame, font=("Helvetica", 10))
        monthly_revenue_entry.insert(0, f'£{monthly_revenue:,.2f}')
        monthly_revenue_entry.grid(row=5, column=3)

        # Monthly Expenditure Section
        # Format bills per room input
        bills_per_room = bills_per_room_entry.get()
        bills_per_room = bills_per_room.replace(',','')
        bills_per_room = float(bills_per_room.replace('£',''))
        bills_per_room_entry.delete(0, END)
        bills_per_room_entry.insert(0, f'£{bills_per_room:,.2f}')

        # Format total bills output
        total_bills = bills_per_room * num_lettable_rooms
        total_bills_entry = Entry(purchase_frame, font=("Helvetica", 10))
        total_bills_entry.insert(0, f'£{total_bills:,.2f}')
        total_bills_entry.grid(row=2, column=5)

        # Format management % input
        management_fee = management_fee_entry.get()
        management_fee = float(management_fee.replace('%',''))
        management_fee_entry.delete(0, END)
        management_fee_entry.insert(0, f'{management_fee:,.1f}%')

        # Format management costs output
        management_costs = (management_fee/100)*monthly_rent_total
        management_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
        management_costs_entry.insert(0, f'£{management_costs:,.2f}')
        management_costs_entry.grid(row=4, column=5)

        # Format insurance input
        insurance = insurance_entry.get()
        insurance = insurance.replace(',','')
        insurance = float(insurance.replace('£',''))
        insurance_entry.delete(0, END)
        insurance_entry.insert(0, f'£{insurance:,.2f}')

        # Format cleaning input
        cleaning = cleaning_entry.get()
        cleaning = cleaning.replace(',','')
        cleaning = float(cleaning.replace('£',''))
        cleaning_entry.delete(0, END)
        cleaning_entry.insert(0, f'£{cleaning:,.2f}')

        # Format void percentage input
        void_percentage = void_percentage_entry.get()
        void_percentage = float(void_percentage.replace('%',''))
        void_percentage_entry.delete(0, END)
        void_percentage_entry.insert(0, f'{void_percentage:,.1f}%')

        # Format void cost output
        void_costs = (void_percentage/100) * monthly_rent_total
        void_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
        void_costs_entry.insert(0, f'£{void_costs:,.2f}')
        void_costs_entry.grid(row=8, column=5)

        # Format maintenance percentage input
        maintenance_percentage = maintenance_percentage_entry.get()
        maintenance_percentage = float(maintenance_percentage.replace('%',''))
        maintenance_percentage_entry.delete(0, END)
        maintenance_percentage_entry.insert(0, f'{maintenance_percentage:,.1f}%')

        # Format maintenance costs output
        maintenance_costs = (maintenance_percentage/100) * monthly_rent_total
        maintenance_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
        maintenance_costs_entry.insert(0, f'£{maintenance_costs:,.2f}')
        maintenance_costs_entry.grid(row=10, column=5)

        # Format mortgage rate input
        mortgage_rate = mortgage_rate_entry.get()
        mortgage_rate = float(mortgage_rate.replace('%',''))
        mortgage_rate_entry.delete(0, END)
        mortgage_rate_entry.insert(0, f'{mortgage_rate}%')

        # Format mortgage costs output
        mortgage_amount = mortgage_amount_entry.get()
        mortgage_amount = mortgage_amount.replace(',','')
        mortgage_amount = mortgage_amount.replace('£','')
        mortgage_amount = float(mortgage_amount)
        mortgage_costs = ((mortgage_rate/100)/12) * mortgage_amount
        mortgage_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
        mortgage_costs_entry.insert(0, f'£{mortgage_costs:,.2f}')
        mortgage_costs_entry.grid(row=12, column=5, pady=20)

        # Calculate and format total expenditure output
        total_expenditure =  total_bills + management_costs + insurance + cleaning + void_costs + maintenance_costs + mortgage_costs
        total_expenditure_entry = Entry(purchase_frame, font=("Helvetica", 10))
        total_expenditure_entry.insert(0, f'£{total_expenditure:,.2f}')
        total_expenditure_entry.grid(row=13, column=5)

        # Summary Column
        # Format price per room output
        price_per_room = total_purchase_costs/num_lettable_rooms
        price_per_room_entry = Entry(purchase_frame, font=("Helvetica", 10))
        price_per_room_entry.insert(0, f'£{price_per_room:,.2f}')
        price_per_room_entry.grid(row=1, column=7)

        # Format gross yield % output 
        gross_yield = ((monthly_rent_total*12)/ total_purchase_costs )*100
        gross_yield_entry = Entry(purchase_frame, font=("Helvetica", 10))
        gross_yield_entry.insert(0, f'{gross_yield:,.1f}%')
        gross_yield_entry.grid(row=2, column=7)

        # Format net yield % output
        net_yield = ((monthly_revenue - total_expenditure)*12/total_purchase_costs)*100
        net_yield_entry = Entry(purchase_frame, font=("Helvetica", 10))
        net_yield_entry.insert(0, f'{net_yield:,.1f}%')
        net_yield_entry.grid(row=3, column=7)

        # Format monthly gross profit output
        monthly_gross = monthly_revenue - total_expenditure
        monthly_gross_entry = Entry(purchase_frame, font=("Helvetica", 10))
        monthly_gross_entry.insert(0, f'£{monthly_gross:,.2f}')
        monthly_gross_entry.grid(row=4, column=7)

        # Format monthly net profit output
        monthly_net = monthly_gross - mortgage_costs
        monthly_net_entry = Entry(purchase_frame, font=("Helvetica", 10))
        monthly_net_entry.insert(0, f'£{monthly_net:,.2f}')
        monthly_net_entry.grid(row=5, column=7)

        # Format annual net profit output
        annual_net = monthly_net * 12 
        annual_net_entry = Entry(purchase_frame, font=("Helvetica", 10))
        annual_net_entry.insert(0, f'£{annual_net:,.2f}')
        annual_net_entry.grid(row=6, column=7)

        # Format occupation to break even output
        occupancy_break_even = (total_expenditure/monthly_revenue)*100
        occupancy_break_even_entry = Entry(purchase_frame, font=("Helvetica", 10))
        occupancy_break_even_entry.insert(0, f'{occupancy_break_even:,.2f}%')
        occupancy_break_even_entry.grid(row=7, column=7)

        # Format return on capital invested output || 
        return_on_capital = (monthly_net/total_capital_employed)*100
        return_on_capital_entry = Entry(purchase_frame, font=("Helvetica", 10))
        return_on_capital_entry.insert(0, f'{return_on_capital}%')
        return_on_capital_entry.grid(row=8, column=7)
        
    else:
        error_label.config(text="You Forgot To Enter Something")

'''
        class Button:
    def __init__(self, name, frame, states="enable"):
        self.label = Label(frame, text=name)
        self.entry = Entry(frame, font=("Helvetica", 10), state = states)
    def reset(self):
        self.entry.insert(0, "")



morgage_ltv = Button(purchase_frame, "sldkfja;s",states = "disable"))
morgage_ltv.label
morgage_ltv.entry
morgage_ltv.reset()
'''

def main():
    # Create global variables
    
    global purchase_section_label
    global purchase_frame_label
    global purchase_frame
    global purchase_section_label
    global purchase_price_label
    global purchase_price_entry
    global mortgage_ltv_label
    global mortgage_ltv_entry
    global mortgage_amount_label
    global mortgage_amount_entry
    global deposit_amount_label
    global deposit_amount_entry
    global stamp_duty_label
    global stamp_duty_entry
    global refurb_costs_label
    global refurb_costs_entry 
    global mortgage_broker_costs_label
    global mortgage_broker_costs_entry
    global survey_vat_costs_label 
    global survey_vat_costs_entry
    global legal_costs_label
    global legal_costs_entry
    global total_capital_employed_label
    global total_capital_employed_entry
    global total_purchase_costs_label
    global total_purchase_costs_entry
    global monthly_rev_section_label
    global num_lettable_rooms_label
    global num_lettable_rooms_entry
    global avg_room_rental_label 
    global avg_room_rental_entry
    global monthly_costs_label 
    global monthly_costs_entry 
    global monthly_rent_total_label 
    global monthly_rent_total_entry 
    global monthly_revenue_label
    global monthly_revenue_entry
    global monthly_expenditure_section_label
    global bills_per_room_label
    global bills_per_room_entry 
    global total_bills_label 
    global total_bills_entry 
    global management_fee_label
    global management_fee_entry
    global management_costs_label 
    global management_costs_entry 
    global insurance_label 
    global insurance_entry 
    global cleaning_label 
    global cleaning_entry
    global void_percentage_label
    global void_percentage_entry
    global void_costs_label
    global void_costs_entry
    global maintenance_percentage_label 
    global maintenance_percentage_entry 
    global maintenance_costs_label
    global maintenance_costs_entry
    global mortgage_rate_label
    global mortgage_rate_entry
    global mortgage_costs_label
    global mortgage_costs_entry
    global total_expenditure_label
    global total_expenditure_entry
    global summary_section_label
    global price_per_room_label
    global price_per_room_entry
    global gross_yield_label
    global gross_yield_entry
    global net_yield_label
    global net_yield_entry
    global monthly_gross_label
    global monthly_gross_entry
    global monthly_net_label
    global monthly_net_entry
    global annual_net_label
    global annual_net_entry
    global occupancy_break_even_label
    global occupancy_break_even_entry
    global return_on_capital_label
    global return_on_capital_entry
    global my_button
    global reset_button
    global error_label
#######################################################################################################
    # Create frame for labels & entries
    purchase_frame_label = LabelFrame(mainframe, text="created by: AstroTechLLC.com")
    purchase_frame_label.pack(pady=10)
    purchase_frame = Frame(purchase_frame_label)
    purchase_frame.grid(row=0, column=0, padx=20, pady=20)


    # Define Labels
    # Purchase Column Labels
    
    purchase_section_label = Label(purchase_frame, text="Purchase", padx=45, bg='yellow', fg='black')
    purchase_section_label.grid(row=0, column=1)

    purchase_price_label = Label(purchase_frame, text="*Purchase Price £", pady=10)
    purchase_price_entry = Entry(purchase_frame, font=("Helvetica", 10))
    purchase_price_label.grid(row=1, column=0)
    purchase_price_entry.grid(row=1, column=1)

    mortgage_ltv_label = Label(purchase_frame, text="*Mortgage LTV %")
    mortgage_ltv_entry = Entry(purchase_frame, font=("Helvetica", 10))
    mortgage_ltv_label.grid(row=2, column=0)
    mortgage_ltv_entry.grid(row=2, column=1)

    mortgage_amount_label = Label(purchase_frame, text="Mortgage £")
    mortgage_amount_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    mortgage_amount_label.grid(row=3, column=0)
    mortgage_amount_entry.grid(row=3, column=1)

    deposit_amount_label = Label(purchase_frame, text="Deposit £")
    deposit_amount_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    deposit_amount_label.grid(row=4, column=0)
    deposit_amount_entry.grid(row=4, column=1, pady=20)

    stamp_duty_label = Label(purchase_frame, text="Stamp Duty £")
    stamp_duty_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    stamp_duty_label.grid(row=5, column=0)
    stamp_duty_entry.grid(row=5, column=1)

    refurb_costs_label = Label(purchase_frame, text="*Refurb Costs £")
    refurb_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
    refurb_costs_label.grid(row=6, column=0)
    refurb_costs_entry.grid(row=6, column=1, pady=20)

    mortgage_broker_costs_label = Label(purchase_frame, text="*Mortgage Brokerage £")
    mortgage_broker_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
    mortgage_broker_costs_label.grid(row=7, column=0)
    mortgage_broker_costs_entry.grid(row=7, column=1)

    survey_vat_costs_label = Label(purchase_frame, text="*Survey inc VAT £")
    survey_vat_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
    survey_vat_costs_label.grid(row=8, column=0)
    survey_vat_costs_entry.grid(row=8, column=1, pady=20)

    legal_costs_label = Label(purchase_frame, text="*Legal Costs £")
    legal_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
    legal_costs_label.grid(row=9, column=0)
    legal_costs_entry.grid(row=9, column=1)

    total_capital_employed_label = Label(purchase_frame, text="Total Capital Employed £")
    total_capital_employed_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    total_capital_employed_label.grid(row=10, column=0)
    total_capital_employed_entry.grid(row=10, column=1, pady=20)

    total_purchase_costs_label = Label(purchase_frame, text="Total Purchase Costs £")
    total_purchase_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    total_purchase_costs_label.grid(row=11, column=0)
    total_purchase_costs_entry.grid(row=11, column=1)


    # Monthly Revenue Column Labels
    monthly_rev_section_label = Label(purchase_frame, text="Monthly Revenue", padx=25, bg='yellow', fg='black')
    monthly_rev_section_label.grid(row=0, column=3)

    num_lettable_rooms_label = Label(purchase_frame, text="*# of Lettable Rooms")
    num_lettable_rooms_entry = Entry(purchase_frame, font=("Helvetica", 10))
    num_lettable_rooms_label.grid(row=1, column=2)
    num_lettable_rooms_entry.grid(row=1, column=3)

    avg_room_rental_label = Label(purchase_frame, text="*Average Room Rental £")
    avg_room_rental_entry = Entry(purchase_frame, font=("Helvetica", 10))
    avg_room_rental_label.grid(row=2, column=2)
    avg_room_rental_entry.grid(row=2, column=3, pady=20)

    monthly_costs_label = Label(purchase_frame, text="*Monthly Costs £")
    monthly_costs_entry = Entry(purchase_frame, font=("Helvetica", 10))
    monthly_costs_label.grid(row=3, column=2)
    monthly_costs_entry.grid(row=3, column=3)

    monthly_rent_total_label = Label(purchase_frame, text="Monthly Rental Total £")
    monthly_rent_total_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    monthly_rent_total_label.grid(row=4, column=2)
    monthly_rent_total_entry.grid(row=4, column=3, pady=20)

    monthly_revenue_label = Label(purchase_frame, text="Monthly Revenue £")
    monthly_revenue_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    monthly_revenue_label.grid(row=5, column=2)
    monthly_revenue_entry.grid(row=5, column=3)


    # Monthly Expenditure Column Labels
    monthly_expenditure_section_label = Label(purchase_frame, text="Monthly Expenditures", padx=10, bg='yellow', fg='black')
    monthly_expenditure_section_label.grid(row=0, column=5)

    bills_per_room_label = Label(purchase_frame, text="*Bills Per Room £")
    bills_per_room_entry = Entry(purchase_frame, font=("Helvetica", 10))
    bills_per_room_label.grid(row=1, column=4)
    bills_per_room_entry.grid(row=1, column=5)

    total_bills_label = Label(purchase_frame, text="Total Bills £")
    total_bills_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    total_bills_label.grid(row=2, column=4)
    total_bills_entry.grid(row=2, column=5)

    management_fee_label = Label(purchase_frame, text="*Management Fee %")
    management_fee_entry = Entry(purchase_frame, font=("Helvetica", 10))
    management_fee_label.grid(row=3, column=4)
    management_fee_entry.grid(row=3, column=5)

    management_costs_label = Label(purchase_frame, text="Management £")
    management_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    management_costs_label.grid(row=4, column=4)
    management_costs_entry.grid(row=4, column=5)

    insurance_label = Label(purchase_frame, text="*Insurance £")
    insurance_entry = Entry(purchase_frame, font=("Helvetica", 10))
    insurance_label.grid(row=5, column=4)
    insurance_entry.grid(row=5, column=5)

    cleaning_label = Label(purchase_frame, text="*Cleaning £")
    cleaning_entry = Entry(purchase_frame, font=("Helvetica", 10))
    cleaning_label.grid(row=6, column=4)
    cleaning_entry.grid(row=6, column=5)

    void_percentage_label = Label(purchase_frame, text="*Void Percentage %")
    void_percentage_entry = Entry(purchase_frame, font=("Helvetica", 10))
    void_percentage_label.grid(row=7, column=4)
    void_percentage_entry.grid(row=7, column=5)

    void_costs_label = Label(purchase_frame, text="Void Costs £")
    void_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    void_costs_label.grid(row=8, column=4)
    void_costs_entry.grid(row=8, column=5)

    maintenance_percentage_label = Label(purchase_frame, text="*Maintenance Percentage %")
    maintenance_percentage_entry = Entry(purchase_frame, font=("Helvetica", 10))
    maintenance_percentage_label.grid(row=9, column=4)
    maintenance_percentage_entry.grid(row=9, column=5)

    maintenance_costs_label = Label(purchase_frame, text="Maintenance Costs £")
    maintenance_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    maintenance_costs_label.grid(row=10, column=4)
    maintenance_costs_entry.grid(row=10, column=5)

    mortgage_rate_label = Label(purchase_frame, text="*Mortgage Rate %")
    mortgage_rate_entry = Entry(purchase_frame, font=("Helvetica", 10))
    mortgage_rate_label.grid(row=11, column=4)
    mortgage_rate_entry.grid(row=11, column=5)

    mortgage_costs_label = Label(purchase_frame, text="Mortgage Costs £")
    mortgage_costs_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    mortgage_costs_label.grid(row=12, column=4)
    mortgage_costs_entry.grid(row=12, column=5, pady=20)

    total_expenditure_label = Label(purchase_frame, text="*Total Expenditures (Monthly) £")
    total_expenditure_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    total_expenditure_label.grid(row=13, column=4)
    total_expenditure_entry.grid(row=13, column=5)


    # Summary Column Labels
    summary_section_label = Label(purchase_frame, text="Summary", padx=45, bg='yellow', fg='black')
    summary_section_label.grid(row=0, column=7)

    price_per_room_label = Label(purchase_frame, text="Price Per Room £")
    price_per_room_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    price_per_room_label.grid(row=1, column=6)
    price_per_room_entry.grid(row=1, column=7)

    gross_yield_label = Label(purchase_frame, text="Gross Yield %")
    gross_yield_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    gross_yield_label.grid(row=2, column=6)
    gross_yield_entry.grid(row=2, column=7)

    net_yield_label = Label(purchase_frame, text="Net Yield %")
    net_yield_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    net_yield_label.grid(row=3, column=6)
    net_yield_entry.grid(row=3, column=7)

    monthly_gross_label = Label(purchase_frame, text="Monthly Gross Profit £")
    monthly_gross_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    monthly_gross_label.grid(row=4, column=6)
    monthly_gross_entry.grid(row=4, column=7)

    monthly_net_label = Label(purchase_frame, text="Monthly Net Profit £")
    monthly_net_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    monthly_net_label.grid(row=5, column=6)
    monthly_net_entry.grid(row=5, column=7)

    annual_net_label = Label(purchase_frame, text="Annual Net Profit £")
    annual_net_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disabled')
    annual_net_label.grid(row=6, column=6)
    annual_net_entry.grid(row=6, column=7)

    occupancy_break_even_label = Label(purchase_frame, text="Occupancy to Break Even %")
    occupancy_break_even_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    occupancy_break_even_label.grid(row=7, column=6)
    occupancy_break_even_entry.grid(row=7, column=7)

    return_on_capital_label = Label(purchase_frame, text="Return on Capital Employed %")
    return_on_capital_entry = Entry(purchase_frame, font=("Helvetica", 10), state='disable')
    return_on_capital_label.grid(row=8, column=6)
    return_on_capital_entry.grid(row=8, column=7)


    # Calculate Button
    my_button = Button(root, text="Calculate Deal", command=calculate)
    my_button.pack(padx=50)


    # Reset Button
    reset_button = Button(root, text="Reset", fg='red', command=reset)
    reset_button.pack(padx=100, pady=15)


    # Error Label
    error_label = Label(mainframe, text="", font=("Helvetica", 14), fg="red")
    error_label.pack(pady=20)


    # Main Loop
    root.mainloop()

main()
