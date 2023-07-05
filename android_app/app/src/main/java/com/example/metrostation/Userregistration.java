package com.example.metrostation;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONObject;

public class Userregistration extends AppCompatActivity implements JsonResponse {
    EditText e1,e2,e3,e4,e5,e6,e7,e8,e9,e10;
    Button b1;

    String fname,lname,gender,dob,address,place,phone,email,user,password,pincode,district;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userregistration);
        e1=(EditText)findViewById(R.id.etfname);
        e2=(EditText)findViewById(R.id.etlname);
        e3=(EditText)findViewById(R.id.address);
//        e4=(EditText)findViewById(R.id.etpin);
//        e10=(EditText)findViewById(R.id.etdis);
        e5=(EditText)findViewById(R.id.etplace);
        e6=(EditText)findViewById(R.id.etphone);
        e7=(EditText)findViewById(R.id.etemail);


        e8=(EditText)findViewById(R.id.etuser);
        e9=(EditText)findViewById(R.id.etpass);
        b1=(Button)findViewById(R.id.button);
//        r1=(RadioButton)findViewById(R.id.radioButton);
//        r2=(RadioButton)findViewById(R.id.radioButton2);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fname=e1.getText().toString();
                lname=e2.getText().toString();
                address=e3.getText().toString();
//                pincode=e4.getText().toString();
//                district=e10.getText().toString();
                place=e5.getText().toString();
                phone=e6.getText().toString();
                email=e7.getText().toString();
                user=e8.getText().toString();
                password=e9.getText().toString();

                if(fname.equalsIgnoreCase("")|| !fname.matches("[a-zA-Z ]+"))
                {
                    e1.setError("Enter your firstname");
                    e1.setFocusable(true);
                }
                else if(lname.equalsIgnoreCase("")|| !lname.matches("[a-zA-Z ]+"))
                {
                    e2.setError("Enter your lastname");
                    e2.setFocusable(true);
                }
                else if(address.equalsIgnoreCase("")|| !address.matches("[a-zA-Z ]+"))
                {
                    e3.setError("Enter your address");
                    e3.setFocusable(true);
                }

                else if(place.equalsIgnoreCase("")|| !place.matches("[a-zA-Z ]+"))
                {
                    e5.setError("Enter your place");
                    e5.setFocusable(true);
                }
                else if(phone.equalsIgnoreCase("") || phone.length()!=10)
                {
                    e6.setError("Enter your phone");
                    e6.setFocusable(true);
                }
                else if(email.equalsIgnoreCase("") || !email.matches("[a-zA-Z0-9._-]+@[a-z]+\\.[a-z]+"))
                {
                    e7.setError("Enter your email");
                    e7.setFocusable(true);
                }
                else if(user.equalsIgnoreCase(""))
                {
                    e8.setError("Enter your username");
                    e8.setFocusable(true);
                }
                else if(password.equalsIgnoreCase(""))
                {
                    e9.setError("Enter your password");
                    e9.setFocusable(true);
                }
                else {
                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) Userregistration.this;
                    String q ="/userregister?fname="+fname+"&lname="+lname+"&place="+place+"&phone="+phone+"&email="+email+"&username="+user+"&password="+password+"&address="+address;
                    q = q.replace(" ","%20");
                    JR.execute(q);
                }
            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {
            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                Toast.makeText(getApplicationContext(), "REGISTRATION SUCCESS", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), login.class));

            } else if (status.equalsIgnoreCase("duplicate")) {
                startActivity(new Intent(getApplicationContext(), Userregistration.class));
                Toast.makeText(getApplicationContext(), "Username and Password already Exist...", Toast.LENGTH_LONG).show();

            } else {
                startActivity(new Intent(getApplicationContext(), Userregistration.class));

                Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }

    }
